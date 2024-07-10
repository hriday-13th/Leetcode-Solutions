class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        d = defaultdict(int)
        for i in t:
            d[i] += 1
            
        req = len(d)
        l, r = 0, 0
        found = 0
        
        slide = defaultdict(int)
        ans = [-1, 0, 0]
        
        while r < len(s):
            c = s[r]
            slide[c] += 1
            
            if c in d and slide[c] == d[c]:
                found += 1
                
            while l <= r and found == req:
                c = s[l]
                
                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]
                    
                slide[c] -= 1
                
                if c in d and slide[c] < d[c]:
                    found -= 1
                    
                l += 1
                
            r += 1
        print(ans)
        return "" if ans[0] == -1 else s[ans[1] : ans[2] + 1]