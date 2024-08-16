class Solution:
    def appealSum(self, s: str) -> int:
        last_seen = {s[0] : 0}
        res = 1
        curr, prev = 0, 1
        
        for i in range(1, len(s)):
            if s[i] in last_seen:
                curr = prev + (i - last_seen[s[i]])
            else:
                curr = prev + (i + 1)
            res += curr
            prev = curr
            last_seen[s[i]] = i
            
        return res