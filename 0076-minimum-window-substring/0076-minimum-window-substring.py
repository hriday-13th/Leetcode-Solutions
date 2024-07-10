class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        counter = defaultdict(int)
        for i in t:
            counter[i] += 1
        req = len(counter)
        
        slider = defaultdict(int)
        l, r = 0, 0
        found = 0
        ans = [-1, 0, 0]
        
        while r < len(s):
            c = s[r]
            slider[c] += 1
            
            if c in counter and slider[c] == counter[c]:
                found += 1
                
            while l <= r and found == req:
                c = s[l]
                
                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]
                    
                slider[c] -= 1
                
                if c in counter and slider[c] < counter[c]:
                    found -= 1
                    
                l += 1
                
            r += 1
            
        return "" if ans[0] == -1 else s[ans[1] : ans[2] + 1]