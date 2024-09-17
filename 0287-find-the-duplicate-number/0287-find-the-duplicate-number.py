class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prev = nums[0]
        
        for i in nums[1:]:
            prev ^= i
            
            if prev == 0:
                return i
            else:
                prev = i
                
        return nums[-1]