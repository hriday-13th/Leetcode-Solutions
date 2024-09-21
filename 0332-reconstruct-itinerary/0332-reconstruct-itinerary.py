class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_map = defaultdict(list)
        res = []
        
        tickets.sort(reverse = True)
        
        for src, dest in tickets:
            adj_map[src].append(dest)
            
        def dfs(st):
            while adj_map[st]:
                next_dest = adj_map[st].pop()
                dfs(next_dest)
            res.append(st)
            
        dfs("JFK")
        return res[::-1]