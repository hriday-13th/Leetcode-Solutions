class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        
        for i in nums:
            if len(res) == 0 or res[-1] < i:
                res.append(i)
            else:
                ind = bisect_left(res, i)
                res[ind] = i
                
        return len(res)