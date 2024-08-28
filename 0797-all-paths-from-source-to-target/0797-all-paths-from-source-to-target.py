class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        end_node = len(graph) - 1
        
        def backtrack(node, path):
            path.append(node)
            if node == end_node:
                res.append(path[:])
            else:
                for c in graph[node]:
                    backtrack(c, path)
            path.pop()
            
        backtrack(0, [])
        return res