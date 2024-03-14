class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        nums = [0] + nums + [0]
        
        res = []
        
        left_sum = 0
        right_sum = sum(nums)
        
        i = 1
        
        while i < len(nums) - 1:
            left_sum += nums[i-1]
            right_sum -= nums[i]
            
            res.append(abs(left_sum - right_sum))
            
            i += 1
            
        return res