from sortedcontainers import SortedList
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if len(vals) == 1:
            return vals[0]

        adj = defaultdict(SortedList)
        
        for i, j in edges:
            adj[i].add(vals[j])
            adj[j].add(vals[i])
            
        res = float('-inf')
        
        for src in range(len(vals)):
            curr_val = vals[src]
            neighbors = sorted(adj[src], reverse=True)[:k]
            curr_val += sum(neighbor for neighbor in neighbors if neighbor > 0)
            res = max(res, curr_val)
        
        return res