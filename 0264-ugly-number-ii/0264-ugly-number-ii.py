class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        t2, t3, t5 = 0, 0, 0
        
        while len(res) < n:
            new = min(2 * res[t2], 3 * res[t3], 5 * res[t5])
            if new not in res:
                res.append(new)
            if new == 2 * res[t2]:
                t2 += 1
            if new == 3 * res[t3]:
                t3 += 1
            if new == 5 * res[t5]:
                t5 += 1
                
        return res[n-1]