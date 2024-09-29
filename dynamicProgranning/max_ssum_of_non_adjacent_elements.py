class Solution:
    def f(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0

        if dp[index] != -1:
            return dp[index]
        
        pick = nums[index] + self.f(index-2, nums, dp)
        not_pick = self.f(index-1, nums, dp)

        return max(pick, not_pick)

    #RECURRENCE - memoization
    def maxnonadjacentsum(self, nums):
        n = len(nums)
        dp = [-1] * (n)
        return self.f(n-1, nums, dp) 
    
    #tabulation
    def maxnonadjacentsum2(self, nums):
        n = len(nums)
        if n == 0:
            return 0  
        if n == 1:
            return nums[0]  
        
        dp = [0] * (n)
        dp[0] = nums[0]
        for i in range(1, n):
            take = nums[i]
            if i > 1:
                take += dp[i-2]
            else:
                non_take = dp[i-1]
            dp[i] = max(take, non_take)
        return dp[-1]

    #space optimization
    def maxnonadjacentsum3(self, nums):
        n = len(nums)
        if n == 0:
            return 0  
        if n == 1:
            return nums[0]  
        
        dp = [0] * (n)
        prev = nums[0]
        prev2 = 0
        for i in range(1, n):
            take = nums[i]
            if i > 1:
                take += prev2
            else:
                non_take = 0 + prev
            curr = max(take, non_take)

            prev2 = prev
            prev = curr
        return prev


def main():
    # Input: list of numbers
    nums = [2, 7, 9, 3, 1]
    
    # Create an object of the Solution class
    solution = Solution()
    
    # Call the maxnonadjacentsum function
    result = solution.maxnonadjacentsum3(nums)
    
    # Print the result
    print(f"The maximum non-adjacent sum is: {result}")

# Run the main function
if __name__ == "__main__":
    main()
