# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left_ht = dfs(node.left)
            right_ht = dfs(node.right)
            
            self.dia = max(self.dia, left_ht + right_ht)
            
            return max(left_ht, right_ht) + 1
        
        self.dia = 0
        dfs(root)
        return self.dia