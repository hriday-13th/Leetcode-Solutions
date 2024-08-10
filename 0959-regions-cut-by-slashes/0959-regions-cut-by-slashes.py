class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1, cols1 = len(grid), len(grid[0])
        rows2, cols2 = 3 * rows1, 3 * cols1
        
        new_grid = [[0] * cols2 for _ in range(cols2)]
        
        for r in range(rows1):
            for c in range(cols1):
                nr, nc = 3*r, 3*c
                if grid[r][c] == "/":
                    new_grid[nr][nc+2] = 1
                    new_grid[nr+1][nc+1] = 1
                    new_grid[nr+2][nc] = 1
                elif grid[r][c] == "\\":
                    new_grid[nr][nc] = 1
                    new_grid[nr+1][nc+1] = 1
                    new_grid[nr+2][nc+2] = 1
                    
        def dfs(r, c, visited):
            if (r < 0 or c < 0  or r >= rows2 or c >= cols2 or new_grid[r][c] != 0 or (r, c) in visited):
                return
            visited.add((r, c))
            neighbors = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]
            
            for i, j in neighbors:
                dfs(i, j, visited)
                
        visited = set()
        res = 0
        
        for i in range(rows2):
            for j in range(cols2):
                if (i, j) not in visited and new_grid[i][j] == 0:
                    dfs(i, j, visited)
                    res += 1
                    
        return res