from collections import deque
#bfs approach
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:    #2D made up of strings
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set() # can use 2D array as well
        islands = 0

        #bfs is an iterative algorithm - use queue
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                #expand our island
                row, col = q.popleft()
                #checking adjacent using loop -- we can go to four directions
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] =="1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # run bfs on this cell
                    bfs(r,c)
                    islands += 1
        
        return islands
    

#dfs approach
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        def dfs(grid, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or grid[i][j] == '-1':
                return

            
            grid[i][j] = '-1'

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    island_count += 1
        return island_count
        



        