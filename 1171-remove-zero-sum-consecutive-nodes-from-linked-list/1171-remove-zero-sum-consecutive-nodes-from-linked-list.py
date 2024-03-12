# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0)
        dum.next = head
        pre_sum = 0
        sum_map = {}
        
        curr = dum
        
        while curr:
            pre_sum += curr.val
            sum_map[pre_sum] = curr
            curr = curr.next
            
        curr = dum
        pre_sum = 0
        
        while curr:
            pre_sum += curr.val
            if pre_sum in sum_map:
                curr.next = sum_map[pre_sum].next
            curr = curr.next
            
        return dum.next