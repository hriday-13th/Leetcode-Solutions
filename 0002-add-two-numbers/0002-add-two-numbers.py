# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = 0, 0
        head1, head2 = l1, l2
        i,j = 0,0

        while (head1 != None):
            n1 += head1.val * (10**i)
            head1 = head1.next
            i += 1

        while (head2 != None):
            n2 += head2.val * (10**j)
            head2 = head2.next
            j += 1

        num = n1 + n2

        ret = ListNode()
        h = ret
        prev = h
        while (num != 0):
            k = num%10
            h.val = k
            temp = ListNode()
            h.next = temp
            prev = h
            h = h.next
            num = (num - k) / 10
        prev.next = None
        return ret