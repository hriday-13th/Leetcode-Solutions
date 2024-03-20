# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        
        for i in range(b + 2):
            if i == a - 1:
                left = curr
            if i == b + 1:
                right = curr
            curr = curr.next
            
        left.next = list2
        
        curr = left.next
        
        while curr.next:
            curr = curr.next
            
        curr.next = right
        
        return list1