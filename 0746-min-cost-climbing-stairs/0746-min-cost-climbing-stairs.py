class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [0] * (n+2)
        
        for i in range(n):
            if i == 0:
                res[i+2] = res[i] + cost[i]
            else:
                res[i+1] = min(res[i+1], res[i] + cost[i])
                res[i+2] = res[i] + cost[i]
                
        return res[-2]