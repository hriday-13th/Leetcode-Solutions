# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        self.pairs = 0
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        self.pairs += 1
                        
            res = [i + 1 for i in left + right]
            return res
        
        dfs(root)
        return self.pairs