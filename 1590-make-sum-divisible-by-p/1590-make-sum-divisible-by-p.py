class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        if target == 0:
            return 0
        
        res = len(nums)
        curr_sum = 0
        
        idx = {0: -1}
        
        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) % p
            prefix = (curr_sum - target + p) % p 
            
            if prefix in idx:
                l = i - idx[prefix]
                res = min(res, l)
                
            idx[curr_sum] = i
            
        return -1 if res == len(nums) else res