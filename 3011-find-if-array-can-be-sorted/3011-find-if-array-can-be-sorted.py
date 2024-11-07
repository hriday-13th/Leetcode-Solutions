class Solution(object):
    def canSortArray(self, nums):
        n = len(nums)
        
        def check(a, b):
            return bin(a).count("1") == bin(b).count("1")
        
        for _ in range(n):
            for i in range(n - 1):
                if check(nums[i], nums[i+1]) and nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    
        return nums == sorted(nums)