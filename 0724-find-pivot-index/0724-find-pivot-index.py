class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left_sum = 0
        right_sum = sum(nums)
        
        nums = [0] + nums + [0]
        i = 1
        
        while i < len(nums) - 1:
            left_sum += nums[i-1]
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i - 1
            
            i += 1
        
        return -1