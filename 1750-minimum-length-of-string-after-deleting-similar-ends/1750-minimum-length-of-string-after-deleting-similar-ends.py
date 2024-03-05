class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n-1
        
        while i < j and s[i] == s[j]:
            ch = s[i]
            while i <= j and s[i] == ch:
                i += 1
            while i <= j and s[j] == ch:
                j -= 1
        if i > j:
            return 0
        else:
            return j-i+1
        
        # while True:
        #     if s[0] == s[-1]:
        #         s = s[1:n-1]
        #     else:
        #         return len(s)