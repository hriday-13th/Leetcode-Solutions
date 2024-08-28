class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for src, dest, time in roads:
            adj[src].append([time, dest])
            adj[dest].append([time, src])
            
        ways = [0] * n
        dist = [float('inf')] * n
        ways[0] = 1
        dist[0] = 0
        
        heap = [(0, 0)]
        
        while heap:
            t, node = heapq.heappop(heap)
            
            for time, nbr in adj[node]:
                newt = t + time
                
                if newt == dist[nbr]:
                    ways[nbr] += ways[node]
                    
                elif newt < dist[nbr]:
                    dist[nbr] = newt
                    heapq.heappush(heap, (newt, nbr))
                    ways[nbr] = ways[node]
                    
        return ways[n-1] % (10 ** 9 + 7)