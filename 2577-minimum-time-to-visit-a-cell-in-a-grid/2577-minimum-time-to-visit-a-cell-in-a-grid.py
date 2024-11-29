class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        
        while heap:
            curr_time, i, j = heapq.heappop(heap)
            
            if i == rows - 1 and j == cols - 1:
                return curr_time
            if (i, j) in visited:
                continue
                
            visited.add((i, j))
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                    wait = 1 if ((grid[ni][nj] - curr_time) % 2 == 0) else 0
                    heapq.heappush(heap, (max(curr_time + 1, grid[ni][nj] + wait), ni, nj))