class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        expr, res = 0, 0
        
        for i in range(len(s)):
            if expr == 0:
                res += int(s[i])
                expr = 1
            elif expr == 1:
                res -= int(s[i])
                expr = 0
                
        return res