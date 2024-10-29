class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 1), (-1, 1)]
        
        @cache
        def dfs(i, j):
            res = 0
            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < rows and 0 <= nj < cols and grid[i][j] < grid[ni][nj]:
                    res = max(res, 1 + dfs(ni, nj))
            return res
        
        return max(dfs(i, 0) for i in range(rows))