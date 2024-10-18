class Solution(object):
    def longestEqualSubarray(self, nums, k):
        count, i = 0, 0
        d = defaultdict(int)
        
        for j in range(len(nums)):
            d[nums[j]] += 1
            count = max(count, d[nums[j]])
            
            if  j - i + 1 - count > k:
                d[nums[i]] -= 1
                i += 1
                
        return count