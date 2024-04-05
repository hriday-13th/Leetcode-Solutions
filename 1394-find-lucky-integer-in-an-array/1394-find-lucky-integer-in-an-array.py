class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        m = -1
        for i in arr:
            d[i] = d.get(i, 0) + 1
        
        for j in d.keys():
            if d[j] == j:
                m = max(m, j)
            
        return m