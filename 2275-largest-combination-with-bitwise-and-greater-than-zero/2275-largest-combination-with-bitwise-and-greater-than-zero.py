class Solution(object):
    def largestCombination(self, candidates):
        res = 0
        
        for bit in range(32):
            count = 0
            for i in candidates:
                if i & 1 << (31 - bit) == 0:
                    continue
                count += 1
            res = max(res, count)
            
        return res