class Solution(object):
    def maxSubArray(self, nums):
        currMax, maxSum = 0, nums[0]
        
        for i in nums:
            currMax = max(currMax + i, i)
            maxSum = max(maxSum, currMax)
            
        return maxSum