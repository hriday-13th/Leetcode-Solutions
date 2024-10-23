# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        level_sum = Counter()
        
        def dfs(node, l):
            if not node:
                return
            level_sum[l] += node.val
            dfs(node.left, l + 1)
            dfs(node.right, l + 1)
            
        dfs(root, 0)
        
        def dfs1(node, l):
            if not node:
                return
            val = level_sum[l+1] - (node.left.val if node.left else 0) - (node.right.val if node.right else 0)
            if node.left:
                node.left.val = val
            if node.right:
                node.right.val = val
            dfs1(node.left, l + 1)
            dfs1(node.right, l + 1)
                
        dfs1(root, 0)
        root.val = 0
        return root