class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        degree = 0
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i, i, 0]
            i1 = min(i, d[nums[i]][0])
            i2 = max(i, d[nums[i]][1])
            i3 = d[nums[i]][2] + 1
            
            d[nums[i]] = [i1, i2, i3]
            degree = max(degree, i3)
            
        res = float('inf')
        for i in d:
            if d[i][2] == degree:
                res = min(res, d[i][1] - d[i][0] + 1)
                
        return res