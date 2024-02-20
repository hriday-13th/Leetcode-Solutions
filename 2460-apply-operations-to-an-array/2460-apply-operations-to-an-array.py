class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        non_zero = 0
        
        for i in nums:
            if i != 0:
                nums[non_zero] = i
                non_zero += 1
                
        while non_zero < len(nums):
            nums[non_zero] = 0
            non_zero += 1
            
        return nums