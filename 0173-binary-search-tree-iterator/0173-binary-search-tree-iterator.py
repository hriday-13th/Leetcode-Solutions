# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = [0]
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.order.append(node.val)
            inorder(node.right)
            
        inorder(root)
        self.itr = 0
        self.len = len(self.order) - 1

    def next(self) -> int:
        self.itr += 1
        return self.order[self.itr]

    def hasNext(self) -> bool:
        if self.itr >= self.len:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()