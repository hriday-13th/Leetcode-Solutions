class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        maxf, i = 0, 0
        d = defaultdict(int)
        
        for j in range(len(nums)):
            d[nums[j]] += 1
            maxf = max(maxf, d[nums[j]])
            
            if j - i + 1 - maxf > k:
                d[nums[i]] -= 1
                i += 1
                
        return maxf