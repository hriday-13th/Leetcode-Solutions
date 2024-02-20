class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nums[0]
        mx, mn = r, r
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mx, mn = mn, mx
                
            mx = max(nums[i], mx * nums[i])
            mn = min(nums[i], mn * nums[i])
            
            r = max(r, mx)
            
        return r