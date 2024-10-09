class Solution(object):
    def countWays(self, nums):
        nums.sort()
        count = 0
        
        if nums[0] > 0:
            count += 1
        if nums[-1] < len(nums):
            count += 1
            
        for i in range(len(nums) - 1):
            s = i + 1
            if nums[i] < s and nums[i + 1] > s:
                count += 1
                
        return count