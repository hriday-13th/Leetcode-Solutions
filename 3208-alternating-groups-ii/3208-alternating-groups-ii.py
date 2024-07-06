class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        color = colors + colors[:k-1]
        count, lo = 0, -1
        
        for hi, (x, y) in enumerate(pairwise(color), 1):
            if x == y:
                lo = hi - 1
            elif hi - lo >= k:
                count += 1
                
        return count