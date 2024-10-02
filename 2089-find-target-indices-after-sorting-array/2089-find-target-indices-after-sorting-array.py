class Solution(object):
    def targetIndices(self, nums, target):
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        
        return res