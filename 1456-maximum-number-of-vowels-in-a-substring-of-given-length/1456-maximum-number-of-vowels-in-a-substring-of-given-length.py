class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vows = "aeiou"
        
        i, j = 0, k
        count = 0
        
        for ele in range(i,j):
            if s[ele] in vows:
                count += 1
                
        res = count
        
        while j < len(s):
            if s[i] in vows:
                count -= 1
            if s[j] in vows:
                count += 1
            res = max(res, count)
            i += 1
            j += 1
            
        return res