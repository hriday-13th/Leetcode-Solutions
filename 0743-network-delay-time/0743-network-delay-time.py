class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        
        for src, dest, wgt in times:
            if src != dest:
                adj[src].append((dest, wgt))
                
        pq = [(0, k)]
        dist = {}
        
        while pq:
            time_taken, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = time_taken
            
            for nbr, time in adj[node]:
                if nbr not in dist:
                    new_time = time_taken + time
                    heapq.heappush(pq, (new_time, nbr))
                    
        if len(dist) != n:
            return -1
        
        return max(dist.values())