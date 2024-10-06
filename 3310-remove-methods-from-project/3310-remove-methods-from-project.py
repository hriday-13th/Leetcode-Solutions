class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        def dfs(node):
            if node not in visited:
                visited.add(node)
                
                for child in adj_list[node]:
                    dfs(child)
                    
        adj_list = [[] for _ in range(n)]
        
        for u, v in invocations:
            adj_list[u].append(v)
            
        visited = set()
        dfs(k)
        
        is_connected = True
        
        for u, v in invocations:
            if v in visited and u not in visited:
                is_connected = False
                
        ans = set(range(n))
        
        return ans - visited if is_connected else ans