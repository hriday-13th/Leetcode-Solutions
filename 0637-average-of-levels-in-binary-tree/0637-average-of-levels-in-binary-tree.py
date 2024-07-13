# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [float(root.val)]
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            child_q = deque()
            temp = 0
            deno = len(q)
            while q:
                node = q.popleft()
                temp += node.val
                if node.left is not None:
                    child_q.append(node.left)
                if node.right is not None:
                    child_q.append(node.right)
                    
            res.append(temp / deno)
            q = child_q
            
        return res