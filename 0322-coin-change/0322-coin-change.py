class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        memo = {}
        ans = self.cal(coins, amt, memo)
        
        return ans if ans != float('inf') else -1
    
    def cal(self, nums: List[int], amt: int, memo: dict[int, int]):
        if amt in memo:
            return memo[amt]
        if amt == 0:
            return 0
        if amt < 0:
            return float('inf')
        
        res = []
        
        for i in nums:
            rem = amt - i
            s = 1 + self.cal(nums, rem, memo)
            if s != float('inf'):
                res.append(s)
        
        memo[amt] = min(res, default=float('inf'))
        return memo[amt]