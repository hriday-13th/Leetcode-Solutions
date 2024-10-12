class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def helper(n):
            if n & 0 == 1:
                return -2
            
            count = 0
            while n > 0 and n & 1 == 1:
                count += 1
                n >>= 1
                
            n <<= count
            if count == 1:
                return n
            n += 1 << (count - 1)
            return n - 1
            
        n = len(nums)
        res = [-1] * n
        
        for i in range(n):
            if nums[i] == 2:
                continue
                
            val = helper(nums[i])
            
            if val == -2:
                return False
            res[i] = val

        return res