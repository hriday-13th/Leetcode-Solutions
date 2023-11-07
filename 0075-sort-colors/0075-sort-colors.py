class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind_zero = 0
        ind_one = nums.count(0)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[ind_zero], nums[i] = nums[i], nums[ind_zero]
                ind_zero += 1
        for j in range(ind_one,len(nums)):
            if nums[j] == 1:
                nums[ind_one], nums[j] = nums[j], nums[ind_one]
                ind_one += 1