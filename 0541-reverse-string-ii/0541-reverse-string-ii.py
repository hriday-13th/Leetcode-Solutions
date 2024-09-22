class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        bit = 0
        
        for i in range(0, len(s), k):
            if bit == 0:
                res += s[i : i + k][::-1]
            else:
                res += s[i : i + k]
            bit = 1 - bit
            
        return res