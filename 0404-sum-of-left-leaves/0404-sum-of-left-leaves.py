# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node:
                return 0
            if not node.left and not node.right:
                if val:
                    return node.val
                else:
                    return 0
                
            left = dfs(node.left, True)
            right = dfs(node.right, False)
            return left + right
        
        return dfs(root, False)