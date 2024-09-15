class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dpPrev = [-float('inf')] * n
        dpCurr = [-float('inf')] * n
        
        for i in range(n):
            dpPrev[i] = a[0] * b[i]
            
        for k in range(1, 4):
            max_val = -float('inf')
            for i in range(k, n):
                max_val = max(max_val, dpPrev[i-1])
                dpCurr[i] = max_val + b[i] * a[k]
            dpPrev = dpCurr.copy()
            
        return max(dpPrev[3:])