class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prime = [True] * 1001
        prime[0] = prime[1] = False
        
        for x in range(2, 1001):
            if prime[x]:
                for i in range(x*x, 1001, x):
                    prime[i] = False
                    
        prev = 0
        
        for i in nums:
            if prev >= i:
                return False
            for j in range(i-1, -1, -1):
                if prime[j] and i - j > prev:
                    break
            prev = i - j
            
        return True