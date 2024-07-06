class MinStack(object):

    def __init__(self):
        self.st = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.st.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.st)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()