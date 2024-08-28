class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end_node = len(graph) - 1
        
        adj = defaultdict(list)
        for i in range(len(graph)):
            adj[i].extend(graph[i])
        
        def backtrack(node, path):
            path.append(node)
            if node == end_node:
                res.append(path.copy())
            else: 
                for child in adj[node]:
                    backtrack(child, path)
            path.pop()
            
        backtrack(0, [])
        return res