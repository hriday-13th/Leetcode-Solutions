# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def build(arr):
            if not arr:
                return None
            
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = build(arr[:mid])
            node.right = build(arr[mid+1:])
            return node
            
        lis = inorder(root)
        return build(lis)