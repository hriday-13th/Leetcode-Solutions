class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        q = deque([(0, 0, k, 0)])
        visited = set()
        
        while q:
            i, j, deletes, steps = q.popleft()
            
            if i == rows - 1 and j == cols - 1:
                return steps
            
            if (i, j, deletes) in visited:
                continue
                
            visited.add((i, j, deletes))
            
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == 0:
                        q.append((ni, nj, deletes, steps + 1))
                    else:
                        if deletes != 0:
                            q.append((ni, nj, deletes - 1, steps + 1))
                            
        return -1