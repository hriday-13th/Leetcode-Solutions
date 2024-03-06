# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        memo = []
        
        curr = head
        memo.append(curr)
        
        while curr is not None:
            curr = curr.next
            if curr not in memo:
                memo.append(curr)
            else:
                return curr
        return None