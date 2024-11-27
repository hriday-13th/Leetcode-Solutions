class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]
        
        def dfs():
            q = deque()
            q.append((0, 0))
            visited = set((0, 0))
            
            while q:
                curr, length = q.popleft()
                if curr == n - 1:
                    return length
                for nbr in adj[curr]:
                    if nbr not in visited:
                        q.append((nbr, length + 1))
                        visited.add(nbr)
                        
        res = []
        for src, dest in queries:
            adj[src].append(dest)
            res.append(dfs())
            
        return res