# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None for _ in range(k)]
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
            
        l, rem = divmod(n, k)
        
        curr = head
        
        for i in range(k):
            part = curr
            size = l + (1 if i < rem else 0)
            
            for _ in range(size - 1):
                if curr:
                    curr = curr.next
                    
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
                
            res[i] = part
            
        return res