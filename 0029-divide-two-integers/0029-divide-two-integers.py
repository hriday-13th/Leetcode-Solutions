class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        
        div = abs(dividend)
        ds = abs(divisor)
        
        res = 0
        
        while div >= ds:
            temp = ds
            mul = 1
            
            while div >= (temp << 1):
                temp <<= 1
                mul <<= 1
                
            div -= temp
            res += mul
            
        return sign * res