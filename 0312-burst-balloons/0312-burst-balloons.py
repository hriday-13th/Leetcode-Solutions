from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i-1] * nums[i] * nums[i+1]
            return max(nums[i-1] * nums[k] * nums[j+1] + dfs(i, k-1) + dfs(k+1, j) for k in range(i, j+1))
                
        return dfs(1, n - 2)