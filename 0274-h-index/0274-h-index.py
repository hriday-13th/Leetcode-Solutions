class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort(reverse=True)
        h = 0
        n = len(c)
        
        while h < n and c[h] > h:
            h += 1
        
        return h