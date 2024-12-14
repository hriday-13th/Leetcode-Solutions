class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def backtrack(i):
            if i >= len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(j+1)
                    path.pop()
                    
        backtrack(0)
        return res