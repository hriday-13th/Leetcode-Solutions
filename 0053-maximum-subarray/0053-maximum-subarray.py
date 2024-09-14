class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local = 0
        globe = nums[0]
        
        for i in nums:
            local += i
            globe = max(globe, local)
            
            if local < 0:
                local = 0
                
        return globe
#         s = 0
#         maxi = nums[0]
        
#         for i in nums:
#             s += i
            
#             maxi = max(maxi, s)
            
#             if s < 0:
#                 s = 0
                
#         return maxi