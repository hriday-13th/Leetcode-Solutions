class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = Counter([0])
        
        for i in nums:
            for k, v in list(dp.items()):
                dp[k | i] += v
                
        return dp[max(dp)]
#         m = defaultdict(int)
        
#         for i in range(1, len(nums) + 1):
#             subsets = list(itertools.combinations(nums, i))
#             for ele in subsets:
#                 m[functools.reduce(lambda x, y: x | y, list(ele))] += 1
                
#         return m[max(m.keys())]