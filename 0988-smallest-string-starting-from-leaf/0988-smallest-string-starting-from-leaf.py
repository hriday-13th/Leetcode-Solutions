# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = None
        self.dfs(root, [])
        return self.ans
    
    def dfs(self, root, path):
        if not root:
            return
        path.append(chr(root.val + ord('a')))
        
        if not root.left and not root.right:
            rev_path = ''.join(path[::-1])
            if self.ans is None or rev_path < self.ans:
                self.ans = rev_path
                
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()