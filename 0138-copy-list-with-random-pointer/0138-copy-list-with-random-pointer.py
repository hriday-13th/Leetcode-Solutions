"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        addr1 = []
        addr2 = []
        
        newList = Node(0, None, None)
        new_curr = newList
        
        curr = head
        while curr:
            addr1.append(curr)
            temp = Node(curr.val, None, None)
            addr2.append(temp)
            new_curr.next = temp
            new_curr = new_curr.next
            curr = curr.next
            
        curr = head
        new_curr = newList.next
        while curr:
            if curr.random is not None:
                x = addr1.index(curr.random)
                new_curr.random = addr2[x]
            curr = curr.next
            new_curr = new_curr.next
            
        return newList.next