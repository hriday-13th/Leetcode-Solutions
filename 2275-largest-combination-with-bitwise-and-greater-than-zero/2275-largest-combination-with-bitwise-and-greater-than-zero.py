class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        
        for bit in range(32):
            count = 0
            for i in range(len(candidates)):
                if candidates[i] & (1 << (31 - bit)) == 0:
                    continue
                count += 1
            res = max(res, count)
        
        return res