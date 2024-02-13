# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = ""
        rev_pal = ""
        while head != None:
            t = head.val
            pal += str(t)
            rev_pal = str(t) + rev_pal
            head = head.next
            
        if pal == rev_pal:
            return True
        else:
            return False