# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import zip_longest
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node, q):
            if not node:
                return
            if not node.left and not node.right:
                q.append(node.val)
            leaves(node.left, q)
            leaves(node.right, q)
            
        l1, l2 = [], []
        leaves(root1, l1)
        leaves(root2, l2)
        
        for a, b in zip_longest(l1, l2):
            if a != b:
                return False
            
        return True