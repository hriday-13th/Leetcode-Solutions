class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(ind, i, j):
            if ind == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[ind]:
                return False
            
            temp = board[i][j]
            board[i][j] = ""
            
            found = (backtrack(ind+1, i+1, j) or backtrack(ind+1, i-1, j) or backtrack(ind+1, i, j+1) or backtrack(ind+1, i, j-1))
            
            board[i][j] = temp
            return found
            
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j):
                        return True
                    
        return False