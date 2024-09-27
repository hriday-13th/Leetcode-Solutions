class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        arr = [0] * 60
        
        for t in time:
            x = t % 60
            res += arr[60 - x] if x > 0 else arr[0]
            arr[x] += 1
            
        return res