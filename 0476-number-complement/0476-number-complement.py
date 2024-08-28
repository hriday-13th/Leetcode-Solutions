class Solution:
    def findComplement(self, num: int) -> int:
        n = str(bin(num))[2:]
        res = ""
        
        for i in n:
            res += "1" if i == "0" else "0"
            
        return int(res, 2)