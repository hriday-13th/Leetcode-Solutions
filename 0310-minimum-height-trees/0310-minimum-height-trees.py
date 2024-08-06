class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges or n == 1:
            return [0]
        
        graph = defaultdict(set)
        
        for src, dest in edges:
            graph[src].add(dest)
            graph[dest].add(src)
            
            
        leaves = []
        for node, children in graph.items():
            if len(children) == 1:
                leaves.append(node)
                
        while n > 2:
            n -= len(leaves)
            next_set = []
            
            for l in leaves:
                u = next(iter(graph[l]))
                graph[u].remove(l)
                if len(graph[u]) == 1:
                    next_set.append(u)
                leaves = next_set
                
        return leaves