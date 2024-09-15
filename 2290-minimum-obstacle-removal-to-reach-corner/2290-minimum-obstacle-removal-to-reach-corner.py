class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
#         q = deque([(0, 0, 0)])
#         visited = set([(0, 0)])
        
#         while q:
#             i, j, count = q.popleft()
            
#             if i == rows - 1 and j == cols - 1:
#                 return count
                
#             for x, y in directions:
#                 ni, nj = i + x, j + y
#                 if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
#                     visited.add((ni, nj))
#                     if grid[ni][nj] == 1:
#                         q.append((ni, nj, count + 1))
#                     else:
#                         q.append((ni, nj, count))
                        
#         return -1
        queue = deque()
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        n = len(grid)
        m = len(grid[0])
        queue.append((0, 0, 0))
        visited.add((0, 0))
        while queue:
            i,j,count = queue.popleft()
            if i == n - 1 and j == m - 1:
                return count
            for x,y in dir:
                dx = x+i
                dy = y+j
                if dx>=0 and dx<n and dy>=0 and dy<m and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    if grid[dx][dy] == 1:
                        queue.append((dx, dy, count + 1))
                    else:
                        queue.appendleft((dx, dy, count))
        return -1