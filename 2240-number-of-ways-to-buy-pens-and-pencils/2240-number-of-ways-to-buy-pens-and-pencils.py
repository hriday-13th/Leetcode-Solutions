class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        lo, hi = min(cost1, cost2), max(cost1, cost2)
        
        for i in range(total, -1, -hi):
            res += i // lo
            
        return res + total // hi + 1