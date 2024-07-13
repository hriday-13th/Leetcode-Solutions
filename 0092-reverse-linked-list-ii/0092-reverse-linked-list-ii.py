# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr= dummy
        
        for _ in range(left - 1):
            curr = curr.next
            
        tail = curr.next
        prev = None
        temp = curr.next
        
        for _ in range(right - left + 1):
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
            
        curr.next = prev
        tail.next = temp
        
        return dummy.next