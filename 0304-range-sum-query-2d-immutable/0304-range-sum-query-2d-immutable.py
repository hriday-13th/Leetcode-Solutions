class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if j != 0:
                    self.matrix[i][j] += self.matrix[i][j-1]
                self.matrix[i][j] += matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        
        for r in range(row1, row2 + 1):
            if col1 == 0:
                res += self.matrix[r][col2]
            else:
                res += self.matrix[r][col2] - self.matrix[r][col1 - 1]
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)