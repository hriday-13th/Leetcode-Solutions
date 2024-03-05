class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_val = -1
        min_val = nums[0]
        
        for i in nums[1:]:
            max_val = max(max_val, i - min_val)
            min_val = min(min_val, i)
            
        return -1 if max_val < 1 else max_val