class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [x for x in nums]
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                nums[j] = (temp[j] + temp[j+1]) % 10
            nums.pop(-1)
            temp = nums
        return nums[0]