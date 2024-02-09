class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums)
        for i in range(len(nums)):
            li = nums[i+1:] + nums[:i]
            flag = True
            for j in li:
                if j > nums[i]:
                    res[i] = j
                    flag = False
                    break
            
        return res