class Solution:
    def findComplement(self, num: int) -> int:
        n = str(bin(num))[2:]
        res = ""
        
        for i in n:
            res += str(1^int(i))
            
        return int(res, 2)