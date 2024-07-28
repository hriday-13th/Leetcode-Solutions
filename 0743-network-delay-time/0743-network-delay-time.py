class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Djikstra Algorithm approach
        adj_list = defaultdict(list)
        
        for u, v, w in times:
            if u != v:
                adj_list[u].append((w, v))
                
        visited = set()
        heap = [(0, k)]
        
        while heap:
            time_taken, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited) == n:
                return time_taken
            
            for time, nbr in adj_list[node]:
                if nbr not in visited:
                    new_time = time + time_taken
                    heapq.heappush(heap, (new_time, nbr))
                    
        return -1