# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, arr):
        if not node:
            return
        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.inorder(root, ans)
        return ans[k-1]