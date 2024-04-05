class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num //= 10
            num = temp
        
        return num