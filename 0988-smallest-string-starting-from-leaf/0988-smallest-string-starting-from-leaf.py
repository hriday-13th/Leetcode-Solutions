# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = None
    def smallestFromLeaf(self, root):
        self.dfs(root, [])
        return self.ans
    
    def dfs(self, node, path):
        if not node:
            return 
        path.append(chr(ord('a') + node.val))
        
        if not node.left and not node.right:
            rev = "".join(path[::-1])
            if not self.ans or rev < self.ans:
                self.ans = rev
                
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        path.pop()