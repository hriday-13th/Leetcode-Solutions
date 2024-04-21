class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, seen):
            if node == destination:
                return True
            seen.add(node)
            for n in graph[node]:
                if n not in seen:
                    if dfs(n, seen):
                        return True
            return False
        
        seen = set()
        return dfs(source, seen)