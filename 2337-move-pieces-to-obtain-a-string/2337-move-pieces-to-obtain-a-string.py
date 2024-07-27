class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        sl = [i for i in range(len(start)) if start[i] == "L"]
        se = [i for i in range(len(start)) if start[i] == "R"]
        tl = [i for i in range(len(target)) if target[i] == "L"]
        te = [i for i in range(len(target)) if target[i] == "R"]
        
        for a, b in zip(sl, tl):
            if a < b:
                return False
            
        for p, q in zip(se, te):
            if p > q:
                return False
            
        return True