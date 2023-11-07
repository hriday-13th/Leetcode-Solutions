# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = []
        
        if head == None or head.next == None:
            return False
        
        curr = head
        while curr != None:
            if curr not in l:
                l += [curr]
                curr = curr.next
            else:
                return True
        return False