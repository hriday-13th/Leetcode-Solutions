class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        sum_val = 0
        max_len = 0
        
        for i, ele in enumerate(nums):
            sum_val += 1 if ele == 1 else -1
            
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in d:
                max_len = max(max_len, i - d[sum_val])
            else:
                d[sum_val] = i
                
        return max_len