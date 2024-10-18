class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        d = {nums[0]: nums[0]}
        curr_key, prev = nums[0], nums[0]
        
        for i in nums[1:]:
            if i - 1 == prev:
                d[curr_key] = i
            else:
                d[i] = i
                curr_key = i
            prev = i
                
        res = []
        for k, v in d.items():
            if k != v:
                res.append(f"{k}->{v}")
            else:
                res.append(f"{k}")
                           
        return res