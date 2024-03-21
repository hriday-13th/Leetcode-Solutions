# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        
        count = 0
        
        def reverse(node):
            prev = None
            itr = node
            
            while itr:
                nex = itr.next
                itr.next = prev
                prev = itr
                itr = nex
            
            return prev, node
            
        count = 0
        while count <= k:
            if curr:
                if count == 0:
                    left_connector = curr
                    curr = curr.next
                    count += 1
                elif count == k:
                    right_connector = curr.next
                    curr.next = None
                    pt1, pt2 = reverse(left_connector.next)
                    left_connector.next = pt1
                    pt2.next = right_connector
                    curr = pt2
                    count = 0
                else:
                    curr = curr.next
                    count += 1
            else:
                break
                
        return dummy.next