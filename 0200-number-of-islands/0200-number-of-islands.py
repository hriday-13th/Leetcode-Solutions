class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.seen = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return
            if (i,j) in self.seen:
                return
            
            self.seen.add((i,j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in self.seen:
                    count += 1
                    dfs(i,j)
        return count