class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxSum, currMax = nums[0], 0
        minSum, currMin = nums[0], 0
        
        for i in nums:
            total += i
            currMax = max(currMax + i, i)
            maxSum = max(maxSum, currMax)
            currMin = min(currMin + i, i)
            minSum = min(minSum, currMin)
            
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum