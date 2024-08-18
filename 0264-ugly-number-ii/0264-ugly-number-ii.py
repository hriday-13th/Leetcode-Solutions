class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2, p3, p5 = 0, 0, 0
        res = [1]
        
        while len(res) != n:
            tba = min(2 * res[p2], 3 * res[p3], 5 * res[p5])
            if tba not in res:
                res.append(tba)
            if tba == 2 * res[p2]:
                p2 += 1
            elif tba == 3 * res[p3]:
                p3 += 1
            elif tba == 5 * res[p5]:
                p5 += 1
                
        print(res)
        return res[-1]