class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def powerFinder(num):
            if num == 1:
                return 1
            elif num % 2 == 0:
                return 1 + powerFinder(num // 2)
            else:
                return 1 + powerFinder(3 * num + 1)
            
        res = []
        for i in range(lo, hi + 1):
            res.append([powerFinder(i), i])
            
        res.sort()
        print(res)
        return res[k-1][1]