class Solution:
    def f(self, index, heights, dp):
        if index == 0:
            return 0
        if dp[index] != -1:
            return dp[index]
     
        left = self.f(index - 1, heights, dp) + abs(heights[index] - heights[index-1])
        
        if index >= 2:
            right = self.f(index - 2, heights, dp) + abs(heights[index] - heights[index-2])
            dp[index] = min(left, right)
        else:
            dp[index] = left
        
        return dp[index]
    

    def frog_jump(self, n, heights):
        dp = [-1] * (n + 1)
        return self.f(n-1, heights, dp)
    

def main():
    # Input parameters
    heights = [10, 30, 40, 20]
    n = len(heights)

    # Create an object of Solution class
    solution = Solution()

    # Call the frog_jump function
    result = solution.frog_jump(n, heights)

    # Print the result
    print(f"Minimum energy needed: {result}")

# Run the main function
if __name__ == "__main__":
    main()
