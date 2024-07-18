# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.map = {}
        self.leaves = []
        self.findLeaves(root, [], self.leaves, self.map)
        res = 0
        for i in range(len(self.leaves)):
            for j in range(i + 1, len(self.leaves)):
                list_i, list_j = self.map[self.leaves[i]], self.map[self.leaves[j]]
                for k in range(min(len(list_i), len(list_j))):
                    if list_i[k] != list_j[k]:
                        dist = len(list_i) - k + len(list_j) - k
                        if dist <= distance:
                            res += 1
                        break
        return res

    def findLeaves(self, node: TreeNode, trail: List[TreeNode], leaves: List[TreeNode], map: Dict[TreeNode, List[TreeNode]]):
        if not node:
            return
        tmp = trail[:]
        tmp.append(node)
        if not node.left and not node.right:
            map[node] = tmp
            leaves.append(node)
            return
        self.findLeaves(node.left, tmp, leaves, map)
        self.findLeaves(node.right, tmp, leaves, map)
#         d = {}
#         leaves = []
        
#         def findleaves(node, trail, leaves, d):
#             if not node:
#                 return
#             temp = trail.copy()
#             temp.append(node)
            
#             if not node.left and not node.right:
#                 d[node] = temp
#                 leaves.append(node)
#                 return
#             findleaves(node.left, temp, leaves, d)
#             findleaves(node.right, temp, leaves, d)
            
#         findleaves(root, [], leaves, d)
#         res = 0
        
#         for i in range(len(leaves)):
#             for j in range(i + 1, len(leaves)):
#                 li, lj = d[leaves[i]], d[leaves[j]]
                
#                 for k in range(min(len(li), len(lj))):
#                     if li[k] != lj[k]:
#                         dist = len(li) - k + len(lj) - k
#                         if dist <= distance:
#                             res += 1
                            
#         return res