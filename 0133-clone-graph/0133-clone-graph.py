"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        
        d = {}
        d[node] = Node(val = node.val)
        
        while q:
            curr = q.popleft()
            for i in curr.neighbors:
                if i not in d:
                    d[i] = Node(val = i.val)
                    q.append(i)
                d[curr].neighbors.append(d[i])
                
        return d[node]