import numpy
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        p1, p2, p3 = sorted(nums,reverse=True)[:3]
        
        rev = [i for i in nums if i < 0]
        
        n1, n2 = sorted(nums)[:2]
        
        if n1 * n2 <= 0:
            return p1 * p2 * p3
        else:
            return max(n1 * n2 * p1, p1 * p2 * p3)
        
#         rep = [i for i in nums if i < 0]
        
#         if len(rep) < 3:
#             return max(nums) * numpy.prod(sorted(rep, reverse=True)[:2])
        
#         return numpy.prod(sorted(nums, reverse=True)[:3])