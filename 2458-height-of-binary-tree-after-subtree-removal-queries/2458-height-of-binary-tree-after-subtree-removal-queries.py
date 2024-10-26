# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        @cache
        def ht(node):
            if not node:
                return 0
            return max(ht(node.left), ht(node.right)) + 1
        
        lookup = {}
        
        def cal(node, depth, m):
            if node is None:
                return
            
            lht = ht(node.left)
            rht = ht(node.right)
            
            if node.left is not None:
                lookup[node.left.val] = max(m, rht + depth)
                cal(node.left, depth + 1, lookup[node.left.val])
            if node.right is not None:
                lookup[node.right.val] = max(m, lht + depth)
                cal(node.right, depth + 1, lookup[node.right.val])
                
        cal(root, 0, 0)
        res = []
        for q in queries:
            res.append(lookup[q])
        return res