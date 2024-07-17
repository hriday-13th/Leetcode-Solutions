# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        
        def dfs(node, flag):
            if not node:
                return None
            to_del = (node.val in to_delete)
            node.left = dfs(node.left, to_del)
            node.right = dfs(node.right, to_del)
            if not to_del and flag:
                res.append(node)
            return None if to_del else node
        
        dfs(root, True)
        return res