import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums.count(i) > math.floor(len(nums) / 3):
                res.append(i)
                
        return list(set(res))