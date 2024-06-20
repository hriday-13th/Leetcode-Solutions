# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cal(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and self.cal(a.left, b.right) and self.cal(a.right, b.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.cal(root.left, root.right)