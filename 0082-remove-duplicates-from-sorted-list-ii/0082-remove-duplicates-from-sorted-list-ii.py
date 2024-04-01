# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        
        curr = head
        while curr:
            seen[curr.val] = seen.get(curr.val, 0) + 1
            curr = curr.next
        
        dum = ListNode(0)
        dum.next = head
        prev = dum
        curr = head
        
        while curr:
            if seen[curr.val] > 1:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                prev.next = curr.next
                # prev = prev.next
                # curr = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        return dum.next