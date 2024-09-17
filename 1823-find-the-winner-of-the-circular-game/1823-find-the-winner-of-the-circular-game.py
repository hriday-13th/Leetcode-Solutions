class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        win = 0
        
        for i in range(1, n + 1):
            win = (win + k) % i
            
        return win + 1