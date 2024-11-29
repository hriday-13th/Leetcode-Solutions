class Solution(object):
    def takeCharacters(self, s, k):
        arr = [0, 0, 0]
        
        for c in s:
            arr[ord(c) - ord('a')] += 1
        
        if min(arr) < k:
            return -1
        
        res = float('inf')
        l = 0
        for r in range(len(s)):
            arr[ord(s[r]) - ord('a')] -= 1
            
            while min(arr) < k:
                arr[ord(s[l]) - ord('a')] += 1
                l += 1
                
            res = min(res, len(s) - (r - l + 1))
            
        return res