class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        prev = None
        
        while j < len(nums):
            if nums[j] != prev:
                nums[i] = nums[j]
                prev = nums[j]
                i += 1
            j += 1
            
        return i