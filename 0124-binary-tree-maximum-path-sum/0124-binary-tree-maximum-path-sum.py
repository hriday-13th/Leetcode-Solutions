# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = float('-inf')
        
    def maxPathSum(self, root):
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                self.ans = max(self.ans, node.val, node.val + left, node.val + right, node.val + left + right)
                return max(node.val, node.val + left, node.val + right)
            else:
                return 0
            
        dfs(root)
        return self.ans