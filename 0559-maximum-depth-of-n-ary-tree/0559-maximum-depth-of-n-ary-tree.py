"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        maxd = 0
        for i in root.children:
            maxd = max(maxd, self.maxDepth(i))
        return maxd + 1