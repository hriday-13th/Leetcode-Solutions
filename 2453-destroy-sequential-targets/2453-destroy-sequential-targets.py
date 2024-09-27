class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d = defaultdict()
        mx = 0
        
        for num in nums:
            x = num % space
            
            if x not in d:
                d[x] = (1, num)
            else:
                d[x] = (d[x][0] + 1, min(d[x][1], num))
            
            mx = max(mx, d[x][0])
            
        res = float('inf')
        for val in d.values():
            if val[0] == mx:
                res = min(res, val[1])
            
        return res