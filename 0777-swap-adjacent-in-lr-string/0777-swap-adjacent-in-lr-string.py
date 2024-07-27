class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        sl = [i for i in range(len(start)) if start[i] == "L"]
        sr = [i for i in range((len(start))) if start[i] == "R"]
        el = [i for i in range(len(end)) if end[i] == "L"]
        er = [i for i in range((len(end))) if end[i] == "R"]
        
        for a, b in zip(sl, el):
            if a < b:
                return False
        
        for p, q in zip(sr, er):
            if p > q:
                return False
            
        return True