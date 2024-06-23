class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        text = text.split()
        words = len(text)
        
        if spaces == 0:
            return text[0]
        if words == 1:
            return text[0] + " " * spaces
        
        needed = spaces // (words - 1)
        extra = spaces % (words - 1)
        
        res = ""
        for i in range(words):
            if i == words-1:
                res += text[i] + " " * extra
            else:
                res += text[i] + " " * needed
            
        return res 