class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """

        l1 = [x for x in range(0,n+1,3)]
        l2 = [x for x in range(0,n+1,5)]
        l3 = [x for x in range(0,n+1,7)]

        return sum(set(l1 + l2 + l3))