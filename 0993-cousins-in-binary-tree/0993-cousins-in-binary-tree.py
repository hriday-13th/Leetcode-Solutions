# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res1, res2 = (-1, None), (-1, None)
    
        def dfs(node, parent, l, x, y):
            nonlocal res1, res2
            if not node:
                return
            if node.val == x:
                res1 = (l, parent)
            if node.val == y:
                res2 = (l, parent)
            dfs(node.left, node, l + 1, x, y)
            dfs(node.right, node, l + 1, x, y)

        dfs(root, None, 0, x, y)
        
        return res1[0] == res2[0] and res1[1] != res2[1]