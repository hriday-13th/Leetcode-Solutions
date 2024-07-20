class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        
        matrix = [[0] * cols for _ in range(rows)]
        
        i, j = 0, 0
        
        while i < rows and j < cols:
            min_val = min(rowSum[i], colSum[j])
            matrix[i][j] = min_val
            rowSum[i] -= min_val
            colSum[j] -= min_val
            
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
                
        return matrix