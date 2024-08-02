class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = nums.count(1)
        
        if count_ones == 0 or count_ones == n:
            return 0
        
        curr = nums[:count_ones].count(1)
        m = curr
        
        for i in range(n):
            curr -= nums[i]
            curr += nums[(i + count_ones) % n]
            m = max(m, curr)
            
        return count_ones - m