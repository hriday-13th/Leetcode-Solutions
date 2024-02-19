import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [x for x in nums]
        if nums.count(0) == 0:
            m = np.prod(temp)
            for i in range(len(nums)):
                nums[i] = m // temp[i]
        else:
            for i in range(len(nums)):
                l = temp[i+1:] + temp[:i]
                nums[i] = np.prod(l)
        return nums