class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        adj = [[i + 1] for i in range(n)]
        
        def dfs():
            q = deque([(0, 0)])
            visited = set((0, 0))
            
            while q:
                node, length = q.popleft()
                if node == n - 1:
                    return length
                for nbr in adj[node]:
                    if nbr not in visited:
                        q.append((nbr, length + 1))
                        visited.add(nbr)
                        
        res = []
        for src, dest in queries:
            adj[src].append(dest)
            res.append(dfs())
            
        return res