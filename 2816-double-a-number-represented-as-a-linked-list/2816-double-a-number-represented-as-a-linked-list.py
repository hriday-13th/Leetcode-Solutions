# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = self.reverse(head)
        carry = 0
        curr, prev = rev, None
        
        while curr:
            new = curr.val * 2 + carry
            curr.val = new % 10
            carry = new // 10
            prev = curr
            curr = curr.next
            
        if carry:
            prev.next = ListNode(carry)
            
        res = self.reverse(rev)
        return res
    
    def reverse(self, node):
        prev, curr = None, node
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        return prev