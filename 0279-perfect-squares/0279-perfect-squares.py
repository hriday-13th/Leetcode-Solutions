class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n + 1):
            req = float('inf')
            j = 1
            while j * j <= i:
                remaining = i - j * j
                req = min(req, dp[remaining])
                j += 1
            dp[i] = req + 1
            
        return dp[n]