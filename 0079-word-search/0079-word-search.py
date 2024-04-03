class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(a, b, c):
            if c == len(word):
                return True
            
            if a < 0 or a >= rows or b < 0 or b >= cols or board[a][b] != word[c]:
                return False
            
            temp = board[a][b]
            board[a][b] = ''
            
            if backtrack(a+1, b, c+1) + backtrack(a-1, b, c+1) + backtrack(a, b+1, c+1) + backtrack(a, b-1, c+1):
                return True
            
            board[a][b] = temp
            return False
            
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False