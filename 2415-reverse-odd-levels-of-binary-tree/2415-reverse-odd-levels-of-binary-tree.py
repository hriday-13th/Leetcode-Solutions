# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque([root])
        is_odd_level = False
        
        while q:
            size = len(q)
            curr_vals = []
            nodes = []
            
            for _ in range(size):
                node = q.popleft()
                nodes.append(node)
                curr_vals.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if is_odd_level:
                curr_vals.reverse()
            
            for i, node in enumerate(nodes):
                node.val = curr_vals[i]
                
            is_odd_level = not is_odd_level
            
        return root