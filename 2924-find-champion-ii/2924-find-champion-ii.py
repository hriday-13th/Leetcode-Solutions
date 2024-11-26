class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = {i : 0 for i in range(n)}
        
        for i, v in edges:
            indegree[v] += 1
            
        count = 0
        res = -1
        
        for i in indegree:
            if indegree[i] == 0:
                count += 1
                res = i
                
        return res if count == 1 else -1