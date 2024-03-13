class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = (n*(n+1)/2) ** 0.5
        
        if x % 1 != 0:
            return -1
        else:
            return int(x)
#         if n == 1:
#             return 1
        
#         l = list(range(1, n + 1))
        
#         for i in range(len(l)):
#             if sum(l[:i+1]) == sum(l[i:]):
#                 return l[i]
#         return -1