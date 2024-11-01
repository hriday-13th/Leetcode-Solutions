class Solution(object):
    def makeFancyString(self, s):
        if len(s) < 3:
            return s
        
        res = s[:2]
        prev1, prev2 = s[1], s[0]
        
        for i in s[2:]:
            if i == prev1 and i == prev2:
                continue
            else:
                res += i
                prev2 = prev1
                prev1 = i
                
        return res