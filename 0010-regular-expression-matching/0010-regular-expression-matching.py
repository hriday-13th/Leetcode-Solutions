import string
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
    
        def cal(i, j, s, p):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i >= len(s) and j >= len(p):
                memo[(i,j)] = True
                return memo[(i,j)]
            
            if j >= len(p):
                memo[(i,j)] = False
                return memo[(i,j)]

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j+1 < len(p) and p[j+1] == "*":
                memo[(i,j)] = cal(i, j + 2, s, p) or (match and cal(i+1, j, s, p))
                return memo[(i,j)]

            if match:
                memo[(i,j)] = cal(i+1, j+1, s, p)
                return memo[(i,j)]

            return False
        
        return cal(0,0,s,p)