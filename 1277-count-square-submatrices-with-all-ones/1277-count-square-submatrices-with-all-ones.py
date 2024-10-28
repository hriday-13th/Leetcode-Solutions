class Solution(object):
    def countSquares(self, matrix):
        count = 0
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    count += 1
                if r == 0 or c == 0:
                    continue
                
                temp = matrix[r][c]
                matrix[r][c] = min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1]) + 1 if matrix[r][c] == 1 else 0
                count += matrix[r][c] - temp
                
        return count