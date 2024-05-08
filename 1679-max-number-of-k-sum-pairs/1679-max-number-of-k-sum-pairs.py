class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        
        res = 0
        
        while i < j:
            val = nums[i] + nums[j]
            
            if val == k:
                res += 1
                i += 1
                j -= 1
            elif val > k:
                j -= 1
            elif val < k:
                i += 1
                
        return res