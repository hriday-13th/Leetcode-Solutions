class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        rot = [x for x in nums][-k:]
        temp = [x for x in nums]
        
        for i in range(len(nums) - k):
            nums[i + k] = temp[i]
            
        for j in range(len(rot)):
            nums[j] = rot[j]