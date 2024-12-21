class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        res = 0
        
        def dfs(curr, parent):
            total = values[curr]
            
            for child in adj[curr]:
                if child != parent:
                    total += dfs(child, curr)
                    
            if total % k == 0:
                nonlocal res
                res += 1
            
            return total
        
        dfs(0, -1)
        return res