class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        
        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            curr *= 10
            for i in range(10):
                dfs(curr + i)
        
        for i in range(1, 10):
            dfs(i)
            
        return res
            