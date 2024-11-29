class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
            
        curr = ""
        res = ""
        m, n = len(str1), len(str2)
        
        for i in range(n):
            curr += str2[i]
            if n % (i + 1) == 0:
                if curr * (m // (i + 1)) == str1 and curr * (n // (i + 1)) == str2:
                    res = curr
                    
        return res