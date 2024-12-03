class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        res = ""
        
        for i in range(len(s)):
            if i in spaces:
                res += " "
            res += s[i]
            
        return res