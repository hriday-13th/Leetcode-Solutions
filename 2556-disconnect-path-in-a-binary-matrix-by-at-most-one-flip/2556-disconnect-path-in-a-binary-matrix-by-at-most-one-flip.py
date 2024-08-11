class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        path = set()
        
        direction = [(1,0), (0,1)]
        
        visited.add((0,0))
        path.add((0,0))
        
        def dfs(i, j):
            if i == rows - 1 and j == cols - 1:
                return True
            
            for a, b in direction:
                ni, nj = i + a, j + b
                if ni < rows and nj < cols and (ni, nj) not in visited and grid[ni][nj] == 1:
                    visited.add((ni, nj))
                    path.add((ni, nj))
                    
                    if dfs(ni, nj):
                        return True
                    
                    path.remove((ni, nj))
                    
            return False
        
        res = dfs(0, 0)
        
        if not res:
            return True
        
        if (0, 0) in path:
            path.remove((0, 0))
        if (rows - 1, cols - 1) in path:
            path.remove((rows - 1, cols - 1))
            
        for p1, p2 in path:
            grid[p1][p2] = 0
            
        visited = set((0, 0))
        
        return not dfs(0, 0)