class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        pre = None
        
        for i in range(len(timeSeries))[::-1]:
            if pre is None:
                res += duration
            else:
                if timeSeries[i] + duration < pre:
                    res += duration
                else:
                    res += pre - timeSeries[i]
            pre = timeSeries[i]
            
        return res