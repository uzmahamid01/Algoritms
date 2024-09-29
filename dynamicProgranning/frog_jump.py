class Solution:
    # def f(self, index, heights, dp):
    #     if index == 0:
    #         return 0
    #     if dp[index] != -1:
    #         return dp[index]
     
    #     left = self.f(index - 1, heights, dp) + abs(heights[index] - heights[index-1])
        
    #     if index >= 2:
    #         right = self.f(index - 2, heights, dp) + abs(heights[index] - heights[index-2])
    #         dp[index] = min(left, right)
    #     else:
    #         dp[index] = left
        
    #     return dp[index]
    
    #tabulation form
    # def frog_jump(self, n, heights):
    #memoization(recurssion form)
    #     # dp = [-1] * (n + 1)
    #     # return self.f(n-1, heights, dp)

    #     dp = [0] * (n)
    #     dp[0] = 0
    #     for i in range(1, n):
    #         fs = dp[i-1] + abs(heights[i] - heights[i-1])
    #         ss = float('inf')
    #         if i > 1:
    #             ss = dp[i-2] + abs(heights[i] - heights[i-2])
    #         dp[i] = min(fs, ss)

    #     return dp[n-1]
    
    #space optimize
    def frog_jump2(self, n, heights):
        prev, prev2 = 0, 0

        for i in range(1, n):
            fs = prev + abs(heights[i] - heights[i-1])
            ss = float('inf')
            if i > 1:
                ss = prev2 + abs(heights[i] - heights[i-2])
            curr = min(fs, ss)
            prev2 = prev
            prev = curr

        return prev

def main():
    # Input parameters
    heights = [10, 30, 40, 20]
    n = len(heights)

    # Create an object of Solution class
    solution = Solution()

    # Call the frog_jump function
    result = solution.frog_jump2(n, heights)

    # Print the result
    print(f"Minimum energy needed: {result}")

# Run the main function
if __name__ == "__main__":
    main()
