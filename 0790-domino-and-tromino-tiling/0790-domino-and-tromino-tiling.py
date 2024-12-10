class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2] + [0] * n
        dpa = [1] * n
        
        for i in range(2, n):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * dpa[i-1]) % 1000000007
            dpa[i] = (dpa[i-1] + dp[i-2]) % 1000000007
            
        return dp[n-1] % 1000000007