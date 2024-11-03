class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for i in range(len(nums)):
            curr = nums[i]
            rem = target - curr
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[curr] = i
