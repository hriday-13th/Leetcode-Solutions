class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        
        for i in range(len(edges)):
            src, dest, prob = edges[i][0], edges[i][1], succProb[i]
            adj[src].append([dest, prob])
            adj[dest].append([src, prob])
            
        pq = [(-1, start_node)]
        visited = set()
        
        while pq:
            prob, node = heapq.heappop(pq)
            visited.add(node)
            
            if node == end_node:
                return -prob 
            
            for nbr in adj[node]:
                if nbr[0] not in visited:
                    heapq.heappush(pq, (nbr[1] * prob, nbr[0]))
                    
        return 0
            