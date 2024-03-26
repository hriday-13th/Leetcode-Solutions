class Solution:
    def arrangeCoins(self, n: int) -> int:
        res, req  = 0, 1
        
        while req <= n:
            res += 1
            n -= req
            req += 1
            
        return res