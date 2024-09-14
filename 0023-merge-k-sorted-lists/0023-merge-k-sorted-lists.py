# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        values, nodes = [], []
        head = dummy
        
        for l in lists:
            if l is not None:
                ind = bisect_left(values, l.val)
                if ind < len(values):
                    values.insert(ind, l.val)
                    nodes.insert(ind, l)
                else:
                    values.append(l.val)
                    nodes.append(l)
                
        while values:
            curr_val = values.pop(0)
            head.next = ListNode(curr_val)
            curr_node = nodes.pop(0)
            
            if curr_node.next != None:
                nex_node = curr_node.next
                new_ind = bisect_left(values, nex_node.val)
                
                if new_ind < len(values):
                    values.insert(new_ind, nex_node.val)
                    nodes.insert(new_ind, nex_node)
                else:
                    values.append(nex_node.val)
                    nodes.append(nex_node)
                    
            head = head.next
            
        return dummy.next
        
#         if not lists:
#             return None
        
#         if len(lists) == 1:
#             return lists[0]
        
#         def merger(head1, head2):
#             new = ListNode(0)
#             curr = new
            
#             while head1 and head2:
#                 if head1. val < head2.val:
#                     curr.next = ListNode(head1.val)
#                     head1 = head1.next
#                 else:
#                     curr.next = ListNode(head2.val)
#                     head2 = head2.next
#                 curr = curr.next
                    
#             if head1:
#                 curr.next = head1
#             if head2:
#                 curr.next = head2
                
#             return new.next
        
#         res = lists[0]
#         for i in range(1, len(lists)):
#             res = merger(res, lists[i])
        
#         return res