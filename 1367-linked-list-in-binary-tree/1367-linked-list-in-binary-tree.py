# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, node):
            if not head:
                return True
            if not node:
                return False
            if node.val != head.val:
                return False
            return dfs(head.next, node.left) or dfs(head.next, node.right)
        
        if not root:
            return False
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == head.val and dfs(head, node):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False