class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        for ele in nums:
            if i == 0 or i == 1 or nums[i-2] != ele:
                nums[i] = ele
                i += 1
        return i