class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        res = [[0] * n for _ in range(n)]
        
        def cal(i, j):
            ans = -1
            for a in range(i, i+3):
                for b in range(j, j+3):
                    if grid[a][b] > ans:
                        ans = grid[a][b]
            return ans
        
        for row in range(n):
            for col in range(n):
                res[row][col] = cal(row, col)
                
        return res