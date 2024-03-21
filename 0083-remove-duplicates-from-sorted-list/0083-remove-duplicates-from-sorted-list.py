# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        prev = None
        curr = head
        seen = []
        
        while curr:
            if curr.val not in seen:
                seen.append(curr.val)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
            
        return head