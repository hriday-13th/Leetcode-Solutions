# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = []
        q = deque([root])
        curr_level = 1
        
        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level_sum.append([curr_sum, curr_level])
            curr_level += 1
            
        level_sum.sort(key=lambda x: (-x[0], x[1]))
        return level_sum[0][1]