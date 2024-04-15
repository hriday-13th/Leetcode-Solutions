# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    l = []
    res = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        self.l.append(str(root.val))
        
        if not root.left and not root.right:
            self.res += int("".join(self.l))
            
        self.sumNumbers(root.left)
        self.sumNumbers(root.right)
        
        self.l.pop()
        
        return self.res