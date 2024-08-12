class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == ".":
                return
            board[r][c] = "."
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
        count = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    dfs(r, c)
                    count += 1
                    
        return count