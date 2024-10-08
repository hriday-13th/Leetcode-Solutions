"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        
        for c in root.children:
            res.extend(self.postorder(c))
            
        res.append(root.val)
        
        return res