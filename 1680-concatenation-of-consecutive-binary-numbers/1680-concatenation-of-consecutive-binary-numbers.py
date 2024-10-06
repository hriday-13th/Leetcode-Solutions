class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 1000000007
        res = 1
        
        for i in range(2, n + 1):
            l = i.bit_length()
            res = (res << l) % mod
            res = (res + i) % mod
        
        return res