# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        def insert(node):
            a, b = node.val, node.next.val
            new_node = ListNode(gcd(a,b))
            new_node.next = node.next
            node.next = new_node
            
        def gcd(m, n):
            return math.gcd(m, n)
            
        curr = head
        
        while curr.next:
            insert(curr)
            curr = curr.next.next
            
        return head