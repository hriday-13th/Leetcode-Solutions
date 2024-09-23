# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_side = ListNode(0)
        right_side = ListNode(0)
        l, r = left_side, right_side

        curr = head
        while curr:
            next_node = curr.next
            if curr.val < x:
                left_side.next = curr
                left_side.next.next = None
                left_side = left_side.next
            else:
                right_side.next = curr
                right_side.next.next = None
                right_side = right_side.next
            curr = next_node
            
        left_side.next = r.next
        
        return l.next