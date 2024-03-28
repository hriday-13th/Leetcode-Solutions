class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = 0
        d = {}
        l = 0
        n = len(nums)
        
        for r in range(n):
            d[nums[r]] = d.get(nums[r], 0) + 1
            if d[nums[r]] > k:
                while nums[l] != nums[r]:
                    d[nums[l]] -= 1
                    l += 1
                d[nums[l]] -= 1
                l += 1
            count = max(r-l+1, count)
        return count