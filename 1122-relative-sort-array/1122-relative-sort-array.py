from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        rem = {}
        
        for i in arr2:
            d[i] = 0
            
        s = sorted(arr1)
        for ele in s:
            if ele in arr2:
                d[ele] += 1
            else:
                rem[ele] = rem.get(ele, 0) + 1
            
        res = []
        
        for i in arr2:
            res.extend([i] * d[i])
            
        for j in rem:
            res.extend([j] * rem[j])
            
        return res