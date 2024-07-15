# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = defaultdict()
        
        for i in descriptions:
            if i[0] not in d:
                d[i[0]] = [TreeNode(i[0]), 0]
            if i[1] not in d:
                d[i[1]] = [TreeNode(i[1]), 0]
            if i[2] == 1:
                d[i[0]][0].left = d[i[1]][0]
                d[i[1]][1] += 1
            if i[2] == 0:
                d[i[0]][0].right = d[i[1]][0]
                d[i[1]][1] += 1
                
        for i in d:
            if d[i][1] == 0:
                return d[i][0]