class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ls = sorted(happiness, reverse=True)
        res = 0
        
        for i in range(k):
            if ls[i] - i > 0:
                res += ls[i] - i
            
        return res