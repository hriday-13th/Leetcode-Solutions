# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twins = deque()
        
        slow, fast = head, head
        res = 0
        
        while slow is not None:
            if fast is not None:
                twins.append(slow.val)
                fast = fast.next.next
            else:
                res = max(res, slow.val + twins.pop())
            slow = slow.next
            
        return res