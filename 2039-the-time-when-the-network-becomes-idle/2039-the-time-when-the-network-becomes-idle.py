class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        adj_list = defaultdict(list)
        
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
            
        shortest = {}
        q = deque([(0, 0)])
        visited = set()
        
        while q:
            node, dist = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            shortest[node] = dist
            
            for nbr in adj_list[node]:
                q.append((nbr, dist + 1))
                
        res = 0
        for i in range(1, len(patience)):
            wait_time = patience[i]
            rtt = 2 * shortest[i]
            last_sec = rtt - 1
            last_packet = (last_sec // wait_time) * wait_time
            last_packet += rtt
            res = max(res, last_packet)
            
        return res + 1