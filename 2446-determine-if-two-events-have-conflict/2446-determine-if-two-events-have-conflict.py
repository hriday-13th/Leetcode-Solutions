class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        h1, h1e = int(event1[0][:2]), int(event1[1][:2])
        m1, m1e = int(event1[0][3:]), int(event1[1][3:])
        
        h2, h2e = int(event2[0][:2]), int(event2[1][:2])
        m2, m2e = int(event2[0][3:]), int(event2[1][3:])
        
        val1, val1e = h1*60 + m1, h1e*60 + m1e
        val2, val2e = h2*60 + m2, h2e*60 + m2e
        
        r1 = list(range(val1, val1e + 1))
        r2 = list(range(val2, val2e + 1))
        
        if val1 in r2 or val1e in r2:
            return True
        elif val2 in r1 or val2e in r1:
            return True
        return False