class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build(equations, values)
        res = []
        
        for src, dest in queries:
            if src not in graph or dest not in graph:
                res.append(-1.0)
            else:
                val = self.bfs(graph, src, dest)
                res.append(val)
                
        return res
        
    def build(self, eq, v):
        graph = defaultdict(dict)
        
        for (s, d), value in zip(eq, v):
            graph[s][d] = value
            graph[d][s] = 1.0 / value
            
        return graph
    
    def bfs(self, graph, s, d):
        q = deque([(s, 1.0)])
        visited = set()
        
        while q:
            node, value = q.popleft()
            
            if node == d:
                return value
            
            visited.add(node)
            
            for child, weight in graph[node].items():
                if child not in visited:
                    q.append((child, weight * value))
                    
        return -1.0