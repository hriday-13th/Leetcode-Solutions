class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        lis = []
        
        for i in timePoints:
            h, m = [int(i) for i in i.split(":")]
            lis.append(h * 60 + m)
            
        lis.sort()
        lis += [1440 + lis[0]]
        res = float('inf')
        prev = lis[0]
        
        for i in lis[1:]:
            res = min(res, abs(i - prev))
            prev = i
            
        return res