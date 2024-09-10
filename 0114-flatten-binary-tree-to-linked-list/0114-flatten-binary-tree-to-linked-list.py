# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        s = []
        
        def tr(node):
            if not node:
                return
            s.append(node)
            tr(node.left)
            tr(node.right)
            
        tr(root)
            
        for i in range(len(s) - 1):
            s[i].left = None
            s[i].right = s[i+1]