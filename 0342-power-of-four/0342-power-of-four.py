class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while (i < n):
            if 4**i < n:
                i += 1
            elif 4**i == n:
                return True
            else:
                return False