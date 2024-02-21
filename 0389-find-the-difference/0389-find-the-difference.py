class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = 0
        
        for i in t:
            count += ord(i)
        for j in s:
            count -= ord(j)
            
        return chr(count)