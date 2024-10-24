class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    if j != 0:
                        grid[i][j] += grid[i][j-1]
                elif j == 0:
                    if i != 0:
                        grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                    
        return grid[-1][-1]
                    