class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        r, c = len(grid), len(grid[0])
        visited = set([(0, 0, health)])
        
        q = deque([(0, 0, health - grid[0][0])])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            i, j, h = q.popleft()
            
            if i == r - 1 and j == c - 1 and h > 0:
                return True
            
            for x, y in directions:
                ni, nj = i + x, j + y
                
                if 0 <= ni < r and 0 <= nj < c:
                    new_h = h - grid[ni][nj]
                    
                    if new_h > 0 and (ni, nj, new_h) not in visited:
                        visited.add((ni, nj, new_h))
                        q.append((ni, nj, new_h))
                        
        return False