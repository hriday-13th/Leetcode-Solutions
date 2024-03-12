# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        def merger(head1, head2):
            new = ListNode(0)
            curr = new
            
            while head1 and head2:
                if head1. val < head2.val:
                    curr.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    curr.next = ListNode(head2.val)
                    head2 = head2.next
                curr = curr.next
                    
            if head1:
                curr.next = head1
            if head2:
                curr.next = head2
                
            return new.next
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = merger(res, lists[i])
        
        return res