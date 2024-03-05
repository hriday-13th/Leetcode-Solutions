# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1, head2 = list1, list2
        merger = ListNode(0)
        curr = merger

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                curr.next = ListNode(head1.val)
                head1 = head1.next
            else:
                curr.next = ListNode(head2.val)
                head2 = head2.next
            curr = curr.next
            
        if head1 is not None:
            curr.next = head1
        if head2 is not None:
            curr.next = head2
            
        return merger.next