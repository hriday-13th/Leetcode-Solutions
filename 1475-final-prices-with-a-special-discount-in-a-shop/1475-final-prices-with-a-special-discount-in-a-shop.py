class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stack = deque()
        
        for i, num in enumerate(prices):
            while stack and stack[-1][1] >= num:
                ind, val = stack.pop()
                res[ind] = val - num
            stack.append((i, num))
        
        return res