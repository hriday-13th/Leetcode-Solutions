class Solution(object):
    def makeFancyString(self, s):
        res = ""
        prev1, prev2 = None, None
        
        for i in s:
            if prev1 == None:
                prev1 = i
                res += i
                continue
            elif prev2 == None:
                prev2 = prev1
                prev1 = i
                res += i
                continue
            elif i == prev1 and i == prev2:
                continue
            else:
                res += i
                prev2 = prev1
                prev1 = i
                
        return res