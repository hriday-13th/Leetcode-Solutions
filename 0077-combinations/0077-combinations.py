class Solution(object):
    def combine(self, n, k):
        def backtrack(start, path, k):
            if k == 0:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path, k - 1)
                path.pop()
                
        res = []
        backtrack(1, [], k)
        return res