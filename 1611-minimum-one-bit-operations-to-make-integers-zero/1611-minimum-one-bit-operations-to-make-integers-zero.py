class Solution:
    def solve(self, n, k):
        if n == 0:
            return k
        b = 1
        
        while (b << 1) < n:
            b *= 2
            
        return self.solve((b // 2) ^ b ^ n, k + b)
        
    def minimumOneBitOperations(self, n: int) -> int:
        return self.solve(n, 0)