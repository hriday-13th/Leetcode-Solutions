# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        crit = []
        
        curr = head.next
        prev = head.val
        ind = 1
        
        while curr.next:
            future = curr.next.val
            if curr.val > prev and curr.val > future:
                crit.append(ind)
            if curr.val < prev and curr.val < future:
                crit.append(ind)
            ind += 1
            prev = curr.val
            curr = curr.next
            
        if len(crit) < 2:
            return [-1, -1]
        
        crit.sort()
        t = float('inf')
        for i in range(1, len(crit)):
            t = min(t, crit[i] - crit[i-1])
            
        return [t, crit[-1] - crit[0]]