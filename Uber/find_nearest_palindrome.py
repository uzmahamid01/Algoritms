class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # Special case for "1"
        if n == "1":
            return "0"
        
        #for values like 999 -> 1001 or 1000 -> 999
        candidates = {str(10**len(n) + 1), str(10**(len(n) - 1) - 1)}
        
        # Get the first half of `n`, adjusted by rounding for mirroring
        prefix = int(n[:(len(n) + 1) // 2])
        
        # Generate palindromic candidates by modifying the prefix
        for i in (prefix - 1, prefix, prefix + 1):
            # Create the palindrome by mirroring the adjusted prefix
            candidate = str(i) + str(i)[-2::-1] if len(n) % 2 else str(i) + str(i)[::-1]
            candidates.add(candidate)

        # Remove the original number itself if present
        candidates.discard(n)

        # Find the closest palindrome by distance, and choose the smallest if distances are the same
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))



        