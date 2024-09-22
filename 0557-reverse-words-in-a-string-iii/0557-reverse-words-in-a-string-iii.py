class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = ""
        
        for w in words:
            res += w[::-1] + " "
        
        return res[:-1]