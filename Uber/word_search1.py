class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):  #i: curr char
            if i == len(word): #found the word
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#" #mark visited

            res = (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or 
                    dfs(r, c+1, i+1) or 
                    dfs(r, c-1, i+1))

            board[r][c] = temp   #unmark the board
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): #start dfs from each cell
                    return True
        return False