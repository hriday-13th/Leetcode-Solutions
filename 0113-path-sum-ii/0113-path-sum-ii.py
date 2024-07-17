# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def count(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [[node.val]]
            
            return [[node.val] + x for x in count(node.left) + count(node.right)]
        
        return [x for x in count(root) if sum(x) == targetSum]
            