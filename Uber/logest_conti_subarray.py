from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_que = deque()
        max_que = deque()
        max_len_subarray = 0
        l = 0

        for r in range(len(nums)):

            while min_que and nums[r] < min_que[-1]:
                min_que.pop()
            min_que.append(nums[r])

            while max_que and nums[r] > max_que[-1]:
                max_que.pop()
            max_que.append(nums[r])

            while max_que[0] - min_que[0] > limit:
                if nums[l] == min_que[0]:
                    min_que.popleft()

                if nums[l] == max_que[0]:
                    max_que.popleft()
                
                l += 1
            
            max_len_subarray = max(max_len_subarray, r-l + 1)
        
        return max_len_subarray 