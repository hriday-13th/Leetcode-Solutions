# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        res = [[root.val]]
        q.append(root)
        
        while q:
            temp = []
            while q:
                node = q.pop(0)
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            q = temp
            dump = [i.val for i in temp]
            res = [dump] + res
            
        return res[1:]