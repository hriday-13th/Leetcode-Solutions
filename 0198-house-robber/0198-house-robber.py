class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        count = 0
        
        for i in range(n):
            res[i] += nums[i]
            for j in range(i, len(res)):
                if j != i + 1:
                    res[j] = max(res[j], res[i])
                    
        return max(res)