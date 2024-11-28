class Solution(object):
    def minimumObstacles(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        q = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        
        while q:
            i, j, breaks = q.popleft()
            if i == rows - 1 and j == cols - 1:
                return breaks
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    if grid[ni][nj] == 1:
                        q.append((ni, nj, breaks + 1))
                    else:
                        q.appendleft((ni, nj, breaks))
            
        return -1