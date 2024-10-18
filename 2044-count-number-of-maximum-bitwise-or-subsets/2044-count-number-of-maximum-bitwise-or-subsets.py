class Solution(object):
    def countMaxOrSubsets(self, nums):
        dp = Counter([0])
        
        for i in nums:
            for k, v in dp.items():
                dp[k | i] += v
                
        return dp[max(dp)]