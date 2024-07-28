"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                    
                for c in node.children:
                    q.append(c)
                    
            res.append(temp)
                
        return res