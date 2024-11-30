class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        connections = defaultdict(deque)
        
        for src, dest in pairs:
            connections[src].append(dest)
            indegree[src] += 0
            indegree[dest] += 1
            outdegree[src] += 1
            outdegree[dest] += 0
            
        start = None
        for i in indegree:
            if outdegree[i] - indegree[i] == 1:
                start = i
                
        if start is None:
            start = list(indegree.keys())[0]
            
        def construct(node):
            while len(connections[node]) > 0:
                curr = connections[node].popleft()
                construct(curr)
                res.append([node, curr])
                
        res = []
        construct(start)
        res.reverse()
        return res