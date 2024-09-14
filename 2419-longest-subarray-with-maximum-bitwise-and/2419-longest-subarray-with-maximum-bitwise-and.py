class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        res, size = 0, 0
        
        for i in nums:
            if i == target:
                size += 1
            else:
                size = 0
            res = max(res, size)
            
        return res