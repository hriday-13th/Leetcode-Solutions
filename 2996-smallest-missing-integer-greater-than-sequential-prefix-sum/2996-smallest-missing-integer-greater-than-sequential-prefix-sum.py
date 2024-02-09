class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        co = nums[0]
        flag = False
        
        if len(nums) == 1:
            return nums[0] + 1
        
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1] + 1:
                flag = True
                break
            else:
                co += nums[j]
                
        while (flag):
            if co in nums:
                co += 1
            else:
                flag = False
                
        return co