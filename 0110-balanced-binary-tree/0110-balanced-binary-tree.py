# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and 1 >= abs(left[1] - right[1]) >= 0
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]