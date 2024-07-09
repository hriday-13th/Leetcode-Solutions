class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        def checker(i, j):
            nonlocal rows, cols
            if i < rows -1 and grid[i][j] != grid[i+1][j]:
                return False
            if j < cols - 1 and grid[i][j] == grid[i][j+1]:
                return False
            return True
        
        for i in range(rows):
            for j in range(cols):
                if not checker(i, j):
                    return False
        return True