class Solution(object):
    def partition(self, s):
        res = []
        paths = []
        
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def backtrack(i):
            if i >= len(s):
                res.append(paths[:])
                return
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    paths.append(s[i:j+1])
                    backtrack(j+1)
                    paths.pop()
                    
        backtrack(0)
        return res