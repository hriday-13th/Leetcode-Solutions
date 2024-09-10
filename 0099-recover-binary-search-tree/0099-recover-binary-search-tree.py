# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes, val = [], []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            val.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        s = sorted(val)
        i1, i2 = None, None
        
        for i in range(len(s)):
            if s[i] != val[i]:
                if i1 is None:
                    i1 = i
                elif i2 is None:
                    i2 = i
        
        nodes[i1].val, nodes[i2].val = nodes[i2].val, nodes[i1].val