# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height_calculator(node):
            if not node:
                return 0
            
            return 1 + max(height_calculator(node.left), height_calculator(node.right))
        
        def filler():
            i, j = 0, (cols - 1) // 2
            matrix[i][j] = str(root.val)
            
            q = deque([(root, i, j)])
            
            while q:
                node, r, c = q.popleft()
                
                if node.left:
                    i, j = r + 1, c - 2 ** (h - r - 2)
                    q.append((node.left, i, j))
                    matrix[i][j] = str(node.left.val)
                    
                if node.right:
                    i, j = r + 1, c + 2 ** (h - r - 2)
                    q.append((node.right, i, j))
                    matrix[i][j] = str(node.right.val)
        
        h = height_calculator(root)
        
        rows, cols = h, (2 ** h) - 1
        matrix = [[""] * cols for _ in range(rows)]
        
        filler()
        
        return matrix