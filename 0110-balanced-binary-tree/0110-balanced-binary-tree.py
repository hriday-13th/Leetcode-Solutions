# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            left_ht = dfs(node.left)
            right_ht = dfs(node.right)
            balanced = left_ht[0] and right_ht[0] and 1 >= (abs(left_ht[1] - right_ht[1])) >= 0
            
            return [balanced, 1 + max(left_ht[1], right_ht[1])]
        
        return dfs(root)[0]