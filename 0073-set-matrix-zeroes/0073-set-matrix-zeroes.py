class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row0 = set()
        col0 = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row0.add(i)
                    col0.add(j)
                    
        for i in range(rows):
            for j in range(cols):
                if i in row0 or j in col0:
                    matrix[i][j] = 0