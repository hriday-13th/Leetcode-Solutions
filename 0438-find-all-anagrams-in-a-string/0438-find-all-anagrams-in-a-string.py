class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        n = len(p)
        pattern = [0] * 26
        for i in p:
            pattern[ord(i) - ord('a')] += 1
            
        res = []
        
        curr_window = [0]* 26
        
        for i in range(n):
            curr_window[ord(s[i]) - ord('a')] += 1
            
        if curr_window == pattern:
            res.append(0)
        
        for r in range(n, len(s)):
            curr_window[ord(s[r - n]) - ord('a')] -= 1
            curr_window[ord(s[r]) - ord('a')] += 1
            if curr_window == pattern:
                res.append(r - n + 1)
                
        return res