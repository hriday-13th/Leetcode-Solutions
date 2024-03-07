# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        curr = head
        mid = head
        prev = None
        count = 0
        
        while curr is not None:
            curr = curr.next
            count += 1
            
        for _ in range(count//2):
            prev = mid
            mid = mid.next
        
        if prev:
            prev.next = mid.next
        else:
            head = mid.next
            
        mid.next = None
        
        return head