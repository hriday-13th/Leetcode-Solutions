class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = sorted(nums, key=lambda x: nums.count(x))
        count = 0
        d = {}
        
        for i in n:
            d[i] = nums.count(i)
            
        last_val = list(d.keys())[-1]
        
        for i in d.keys():
            if d[i] == d[last_val]:
                count += d[last_val]
        return count