# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for _ in range(m)]
        
        rs, rl = 0, m - 1
        cs, cl = 0, n - 1
        
        i, j = 0, 0
        
        curr = head
        
        while curr:
            for j in range(cs, cl + 1):
                if curr:
                    grid[rs][j] = curr.val
                    curr = curr.next
            rs += 1

            for i in range(rs, rl + 1):
                if curr:
                    grid[i][cl] = curr.val
                    curr = curr.next
            cl -= 1

            for j in range(cl, cs - 1, -1):
                if curr:
                    grid[rl][j] = curr.val
                    curr = curr.next
            rl -= 1

            for i in range(rl, rs - 1, -1):
                if curr:
                    grid[i][cs] = curr.val
                    curr = curr.next
            cs += 1
            
        return grid