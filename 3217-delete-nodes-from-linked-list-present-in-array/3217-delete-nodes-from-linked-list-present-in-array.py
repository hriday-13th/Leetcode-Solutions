# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        
        while head and head.val in nums:
            head = head.next
            
        if not head:
            return None
        
        curr = head.next
        prev = head
        
        while curr:
            if curr.val not in nums:
                prev.next = curr
                prev = curr
            curr = curr.next
            
        prev.next = None
        return head
#         dummy = ListNode(0)
#         dummy.next = head
#         curr = head
#         prev = dummy
        
#         while curr:
#             if curr.val in nums:
#                 prev.next = curr.next
#                 curr.next = None
#                 curr = prev.next
#             else:
#                 prev = curr
#                 curr = curr.next
        
#         return dummy.next