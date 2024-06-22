class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1] if prices[i] - prices[i-1] > 0 else 0
            dp[i] = dp[i-1] + diff
                
        return dp[-1]
#         i = 0
#         profit = 0
#         buy = 0
        
#         while i < len(prices) - 1:
#             if prices[i] <= prices[i+1]:
#                 if buy == 0:
#                     buy = prices[i]
#                 while i < len(prices) - 1 and prices[i] <= prices[i+1]:
#                     i += 1
#                 profit += prices[i] - buy
#                 buy = 0
#             i += 1
        
#         return profit