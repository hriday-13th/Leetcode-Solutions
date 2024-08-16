class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_max, global_min = arrays[0][-1], arrays[0][0]
        res = 0
        
        for i in arrays[1:]:
            local_max, local_min = i[-1], i[0]
            res = max(res, max(global_max - local_min, local_max - global_min))
            global_max = max(global_max, local_max)
            global_min = min(global_min, local_min)
            
        return res