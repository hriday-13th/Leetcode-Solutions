class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        
        while i < len(nums) - 1:
            count += 1
            jump = 0
            
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums) - 1:
                    return count
                elif i + j + nums[i + j] > jump:
                    jump = i + j + nums[i + j]
                    nex = i + j
            i = nex
        
        return count
        
        # while i < len(nums):
        #     m = max(nums[i + 1 : nums[i] + 1])
        #     j = nums.index(m)
        #     if j + m >= len(nums) - 1:
        #         return count + 1
        #     i = j
        #     count += 1
            