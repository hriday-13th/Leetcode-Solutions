# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node, is_left, curr_count):
            nonlocal res
            if not node:
                return
            res = max(res, curr_count)
            
            if is_left:
                dfs(node.left, True, 1)
                dfs(node.right, False, curr_count + 1)
            else:
                dfs(node.left, True, curr_count + 1)
                dfs(node.right, False, 1)
                
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        
        return res