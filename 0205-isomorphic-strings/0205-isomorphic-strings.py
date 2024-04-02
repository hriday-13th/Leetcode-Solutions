class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        
        for i in range(len(s)):
            if s[i] not in d1 and t[i] not in d2:
                d1[s[i]] = i
                d2[t[i]] = i
                
            elif s[i] in d1 and t[i] in d2:
                if d1[s[i]] != d2[t[i]]:
                    return False
                d1[s[i]] = i
                d2[t[i]] = i
            
            else:
                return False
        
        return True