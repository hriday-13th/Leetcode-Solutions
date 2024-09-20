class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix = 0, 0
        base = 29
        last_index = 0
        mod = 10 ** 9 + 7
        power = 1
        
        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1)
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            suffix = (suffix + char * power) % mod
            power = (power * base) % mod
            
            if prefix == suffix:
                last_index = i
                
        suffix = s[last_index + 1:]
        return suffix[::-1] + s
#         l = 2 * len(s) - 1
#         res = ""
        
#         def is_pal(s, l, r):
#             while l <= r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True
        
#         for r in reversed(range(len(s))):
#             if is_pal(s, 0, r):
#                 return s[r+1:][::-1] + s
            
#         return ""