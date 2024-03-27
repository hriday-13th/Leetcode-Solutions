import numpy
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left, right = 0, 0
        count = 0
        prod = 1
        
        n = len(nums)
        
        while right < n:
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1
            
        return count