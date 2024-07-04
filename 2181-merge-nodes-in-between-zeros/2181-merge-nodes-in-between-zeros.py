# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        
        curr = head.next
        s = 0

        while curr:
            if curr.val == 0:
                temp.next = ListNode(s)
                temp = temp.next
                s = 0
            else:
                s += curr.val
            curr = curr.next
        
        return dummy.next