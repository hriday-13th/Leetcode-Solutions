class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        r1, c1 = ord(s[0]), int(s[1])
        r2, c2 = ord(s[3]), int(s[4])
        res = []
        
        for r in range(r1, r2 + 1):
            char = chr(r)
            for c in range(c1, c2 + 1):
                res.append(char + str(c))
                
        return res