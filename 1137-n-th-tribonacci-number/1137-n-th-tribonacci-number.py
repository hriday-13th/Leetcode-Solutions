class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.trib(n, memo)
    
    def trib(self, n: int, memo: dict[int, int]):
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        if n not in memo:
            memo[n] = self.trib(n-1, memo) + self.trib(n-2, memo) + self.trib(n-3, memo)
        return memo[n]