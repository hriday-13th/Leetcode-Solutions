class Solution(object):
    def lengthOfLIS(self, nums):
        res = []
        
        for i in nums:
            if not res or res[-1] < i:
                res.append(i)
            else:
                ind = bisect_left(res, i)
                res[ind] = i
                
        return len(res)