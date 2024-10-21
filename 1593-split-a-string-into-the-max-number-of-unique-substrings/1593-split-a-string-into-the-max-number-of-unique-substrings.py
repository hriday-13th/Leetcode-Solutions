class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        
        def backtrack(start, seen):
            if start == n:
                return 0
            res = 0
            for end in range(start + 1, n + 1):
                sub = s[start : end]
                if sub not in seen:
                    seen.add(sub)
                    res = max(res, 1 + backtrack(end, seen))
                    seen.remove(sub)
            
            return res
        
        return backtrack(0, set())