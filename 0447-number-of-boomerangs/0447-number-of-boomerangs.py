class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        
        for i0, i1 in points:
            d = {}
            for j0, j1 in points:
                dist = ((j1 - i1) ** 2 + (j0 - i0) ** 2) ** 0.5
                d[dist] = d.get(dist, 0) + 1
                
            for val in d.values():
                count += val * (val - 1)
                
        return count