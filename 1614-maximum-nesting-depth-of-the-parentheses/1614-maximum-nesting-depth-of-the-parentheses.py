class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s) == 1:
            return 0
        ls = list(s)[::-1]
        m = 0
        count = 0
        
        for i in range(len(ls)):
            if ls[i] == ")":
                count += 1
                m = max(m, count)
            elif ls[i] == "(":
                count -= 1
                m = max(m, count)
            else:
                continue
                
        return m