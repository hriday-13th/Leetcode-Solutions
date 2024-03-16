class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        n = len(nums)
        
        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                if i != correct and nums[i] not in res:
                    res.append(nums[i])
                i += 1
                
        return res