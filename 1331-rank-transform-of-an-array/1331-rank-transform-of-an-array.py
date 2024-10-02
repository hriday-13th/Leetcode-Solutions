class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = []
        
        d = defaultdict(int)
        
        new_arr = sorted(arr)
        rank = 1
        
        for i, ele in enumerate(new_arr):
            if ele in d:
                continue
            else:
                d[ele] = rank
                rank += 1
                
        for i in arr:
            res.append(d[i])
            
        return res