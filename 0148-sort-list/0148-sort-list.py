# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.merge(left, right)
    
    def merge(self, a, b):
        dumm = ListNode(0)
        res = dumm
        
        while a and b:
            if a.val < b.val:
                res.next = a
                a = a.next
            else:
                res.next = b
                b = b.next
            res = res.next
        
        res.next = a if a else b
        return dumm.next