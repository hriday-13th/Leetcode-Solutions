class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        high = -sys.maxsize-1
        till = 0
        
        for i in range(len(nums)):
            till += nums[i]
            
            if high < till:
                high = till
            
            if till < 0:
                till = 0
                
        return high