class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        if k == 0:
            return 1
        
        bits = [0] * 32
        l = 0
        res = float('inf')
        n = len(nums)
        
        for r in range(n):
            curr = 0
            for i in range(32):
                if nums[r] & (1 << i):
                    bits[i] += 1
                if bits[i] > 0:
                    curr |= (1 << i)
                    
            if curr >= k:
                res = min(res, r - l + 1)
                
            while curr >= k:
                curr = 0
                for i in range(32):
                    if nums[l] & (1 << i):
                        bits[i] -= 1
                    if bits[i] > 0:
                        curr |= (1 << i)
                l += 1
                if curr >= k:
                    res = min(res, r - l + 1)
                    
        return res if res != float('inf') else -1