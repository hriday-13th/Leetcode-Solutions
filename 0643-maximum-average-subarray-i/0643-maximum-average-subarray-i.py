class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / len(nums)
        
        i, j = 0, k
        avg = sum(nums[i:j]) / k
        res = avg
        
        while j < len(nums):
            avg += (nums[j] - nums[i]) / k
            res = max(res, avg)
            i += 1
            j += 1
            
        return res