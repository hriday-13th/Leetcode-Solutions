class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        ls = s.split()
        
        if len(pattern) != len(ls):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                if ls[i] not in d.values():
                    d[pattern[i]] = ls[i]
                else:
                    return False
            elif d[pattern[i]] != ls[i]:
                    return False
                
        return True