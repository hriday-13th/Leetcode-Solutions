class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        
        count = 0
        
        for i in range(row):
            count += mat[i][i]
            if row - i - 1 != i:
                count += mat[row - i - 1][i]
                
        return count