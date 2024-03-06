class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        buy = 0
        
        while i < len(prices) - 1:
            if prices[i] <= prices[i+1]:
                if buy == 0:
                    buy = prices[i]
                while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                    i += 1
                profit += prices[i] - buy
                buy = 0
            i += 1
#             if prices[i] > prices[i+1]:
#                 if buy > 0:
#                     profit = prices[i] - buy
#                     buy = 0
                    
#             elif prices[i] <= prices[i+1]:
#                 if buy == 0:
#                     buy = prices[i]
#                 while i < len(prices) - 1 and prices[i] <= prices[i+1]:
#                     i += 1
#                 profit += prices[i] - buy
#                 buy = 0
#             i += 1
        
        return profit