class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        max_len = max(len(i) for i in words)
        res = [""] * max_len
        
        for i in range(max_len):
            for word in words:
                if i < len(word):
                    res[i] += word[i]
                else:
                    res[i] += " "
                    
        return [w.rstrip() for w in res]