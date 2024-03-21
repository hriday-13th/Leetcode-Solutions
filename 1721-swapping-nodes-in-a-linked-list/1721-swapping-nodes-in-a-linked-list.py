# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        l = 0
        curr = head
        
        while curr:
            curr = curr.next
            l += 1
            
        if k-1 == l-k:
            return head
        
        curr = head
        pt1, pt2 = None, None
        for i in range(l):
            if i == k-1:
                pt1 = curr
            elif i == l-k:
                pt2 = curr
            curr = curr.next
            
        pt1.val, pt2.val = pt2.val, pt1.val
        return head