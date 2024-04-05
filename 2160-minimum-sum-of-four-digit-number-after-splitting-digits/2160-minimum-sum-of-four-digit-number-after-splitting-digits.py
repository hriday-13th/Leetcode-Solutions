class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted([int(i) for i in str(num)])
        
        f = s[0]*10 + s[-1]
        s = s[1]*10 + s[-2]
        
        return f + s