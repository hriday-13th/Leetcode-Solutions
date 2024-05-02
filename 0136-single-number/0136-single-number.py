class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in nums:
            res ^= i
            
        return res
        # for i in nums:
        #     if nums.count(i) == 1:
        #         return i