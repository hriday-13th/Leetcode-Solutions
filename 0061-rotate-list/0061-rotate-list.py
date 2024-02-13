# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        count = 1
        temp = head
        while temp.next is not None:
            temp = temp.next
            count += 1
        
        k = k % count
        
        if k == 0:
            return head
        
        place_holder = head
        for i in range(count - k -1):
            place_holder = place_holder.next
        new_head = place_holder.next
        place_holder.next = None
        temp.next = head

        return new_head