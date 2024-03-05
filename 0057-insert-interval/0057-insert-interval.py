class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x = intervals + [newInterval]
        inter = sorted(x, key=lambda x: x[0])
        
        res = []

        for i in range(len(inter)):
            curr = inter[i]

            if not res or curr[0] > res[-1][1]:
                res.append(curr)
            else:
                res[-1][1] = max(res[-1][1], curr[1])

        return res