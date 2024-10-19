class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        
        def dfs(i, j):
            temp = float('inf')
            
            for k in range(i + 1, j):
                temp = min(temp, values[i] * values[j] * values[k] + dfs(i, k) + dfs(k, j))
                
            if temp == float('inf'):
                return 0
            
            return temp
        
        return dfs(0, len(values) - 1)