class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_val = 0
        
        for i in prices[1:]:
            max_val = max(max_val, i - min_val)
            min_val = min(min_val, i)
        
        return max_val