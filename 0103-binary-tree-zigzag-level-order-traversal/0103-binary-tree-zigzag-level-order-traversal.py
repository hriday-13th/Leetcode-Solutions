# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        flip = 0
        q = [root]
        
        while q:
            size = len(q)
            t = []
            
            for i in range(size):
                node = q.pop(0)
                t.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if flip == 0:
                res.append(t)
            else:
                res.append(t[::-1])
            flip = 1 - flip
                    
        return res