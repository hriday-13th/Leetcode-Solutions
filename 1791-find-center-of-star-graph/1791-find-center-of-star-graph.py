class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
#         d = collections.defaultdict()
        
#         for ele in edges:
#             d[ele[0]] = d.get(ele[0], 0) + 1
#             d[ele[1]] = d.get(ele[1], 0) + 1
            
#         for i in d:
#             if d[i] == len(edges) - 1:
#                 return i