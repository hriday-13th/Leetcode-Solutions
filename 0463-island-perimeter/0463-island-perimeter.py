class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0:
                return 1
            
            if (i,j) in seen:
                return 0
            
            seen.add((i,j))
            ans = dfs(i, j+1)
            ans += dfs(i, j-1)
            ans += dfs(i+1, j)
            ans += dfs(i-1, j)
            return ans
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)