# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr = head
        res = 0
        
        while curr:
            if len(nums) == 0:
                return res
            if curr.val in nums:
                while curr and curr.val in nums:
                    nums.remove(curr.val)
                    curr = curr.next
                res += 1
            else:
                curr = curr.next
                
        return res