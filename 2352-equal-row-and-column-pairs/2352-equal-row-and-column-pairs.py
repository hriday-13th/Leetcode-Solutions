class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows, cols = defaultdict(lambda : 0), defaultdict(lambda : 0)
        
        for row in grid:
            s = ".".join([str(i) for i in row])
            rows[s] += 1
            
        for col in range(n):
            s = ""
            for r in range(n + 1):
                if r == n:
                    cols[s[:-1]] += 1
                else:
                    s += str(grid[r][col]) + "."
                
        count = 0
        for i in rows:
            count += rows[i] * cols[i]
            
        return count