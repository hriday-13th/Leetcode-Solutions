class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = [[y for y in x] for x in matrix]
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = temp[i][j]