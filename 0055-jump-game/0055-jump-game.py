class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = 0
        
        for n in nums:
            if h < 0:
                return False
            elif h < n:
                h = n
            h -= 1
            
        return True