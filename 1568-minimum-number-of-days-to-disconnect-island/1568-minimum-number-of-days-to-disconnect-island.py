class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c, visited):
            if 0 > r or r == rows or 0 > c or c == cols or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r - 1, c, visited)
            dfs(r, c - 1, visited)
            
        def countIslands():
            visited = set()
            count = 0
            for r in range(rows):
                for c in range(cols):
                    if (r, c) not in visited and grid[r][c] == 1:
                        dfs(r, c, visited)
                        count += 1
                        
            return count, visited
                    
        count, visited = countIslands()
        
        if count != 1:
            return 0
        
        for r, c in visited:
            grid[r][c] = 0
            
            count, visit2 = countIslands()
            if count != 1:
                return 1
            
            grid[r][c] = 1
        
        return 2