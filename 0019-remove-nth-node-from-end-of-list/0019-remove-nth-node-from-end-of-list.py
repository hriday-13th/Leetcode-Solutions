# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        axe = head
        h = head
        
        if head.next is None:
            return None
        
        while n != 0 and head is not None:
            head = head.next
            n -= 1
            
        if head is None and n > 0:
            return h
        
        if head is None and n == 0:
            return h.next
        
        while head is not None:
            prev = axe
            axe = axe.next
            head = head.next
            
        prev.next = axe.next
        axe.next = None
        
        return h