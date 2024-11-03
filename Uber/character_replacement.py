class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        res = 0
        left = 0
        right = 0
        maxf = 0

        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            #if the number of character replace exceeds then move the left pointer
            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
                
            
            res = max(res, right - left + 1)
        return res