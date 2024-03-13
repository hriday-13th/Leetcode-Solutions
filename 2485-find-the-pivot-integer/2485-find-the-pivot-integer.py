class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        l = list(range(1, n + 1))
        
        for i in range(len(l)):
            if sum(l[:i+1]) == sum(l[i:]):
                return l[i]
        return -1