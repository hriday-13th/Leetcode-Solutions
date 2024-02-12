import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > math.floor(len(nums)/2):
                return i