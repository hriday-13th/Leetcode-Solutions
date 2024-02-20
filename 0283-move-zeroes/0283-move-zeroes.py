class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        
        for i in nums:
            if i != 0:
                nums[non_zero] = i
                non_zero += 1
                
        while non_zero < len(nums):
            nums[non_zero] = 0
            non_zero += 1
        
        
#         zero_pointer = 0
        
#         while zero_pointer != len(nums) and len(nums) > 1:
#             if nums[zero_pointer] != 0:
#                 zero_pointer += 1
#             else:
#                 non_zero_pointer = zero_pointer + 1
#                 while non_zero_pointer < len(nums) and nums[non_zero_pointer] == 0:
#                     non_zero_pointer += 1
#                 if non_zero_pointer < len(nums):
#                     nums[zero_pointer], nums[non_zero_pointer] = nums[non_zero_pointer], nums[zero_pointer]
#                 zero_pointer += 1