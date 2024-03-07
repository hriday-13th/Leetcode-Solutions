class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return self.cal(n, memo)
    
    def cal(self, n: int, memo: dict[int,int]):
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        if n not in memo:
            memo[n] = self.cal(n-1, memo) + self.cal(n-2, memo)
        return memo[n]