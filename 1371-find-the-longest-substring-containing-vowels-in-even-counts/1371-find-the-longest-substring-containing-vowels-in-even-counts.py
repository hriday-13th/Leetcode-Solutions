class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        
        mask_to_idx = {0 : -1}
        mask = 0
        res = 0
        
        for i, c in enumerate(s):
            if c in vowels:
                mask ^= 1 + (ord(c) - ord('a'))
            if mask in mask_to_idx:
                l = i - mask_to_idx[mask]
                res = max(res, l)
            else:
                mask_to_idx[mask] = i
                
        return res