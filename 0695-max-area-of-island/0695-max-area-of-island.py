class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        
        def area(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            
            return 1 + area(r + 1, c) + area(r, c + 1) + area(r - 1, c) + area(r, c - 1)
            
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    arr = area(r, c)
                    max_area = max(max_area, arr)
                    
        return max_area