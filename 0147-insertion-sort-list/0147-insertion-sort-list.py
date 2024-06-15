# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-float('inf'))
        
        while head:
            prev = None
            nex = head.next
            tail = dummy
            
            while tail and tail.val < head.val:
                prev = tail
                tail = tail.next
                
            prev.next = head
            head.next = tail
            head = nex
        
        return dummy.next