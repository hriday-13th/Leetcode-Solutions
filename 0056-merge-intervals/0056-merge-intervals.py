class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inters = sorted(intervals, key= lambda x: x[0])
        res = [inters[0]]
        
        for i in range(1, len(inters)):
            current_interval = inters[i]
            last_merged = res[-1]

            if current_interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                res.append(current_interval)
        
#         i = 0
        
        # while i < len(inters) - 1:
        #     l = inters[i]
        #     while inters[i+1][0] <= l[1]:
        #         l[1] = inters[i+1][1]
        #         i += 1
        #     res.append(l)
        #     i += 1
        # if i < len(inters):
        #     res.append(inters[-1])
        return res