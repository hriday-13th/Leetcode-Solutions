class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def isdiv(num):
            res = mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ac + mid//abc
            return res >= n
        
        ab = a*b // math.gcd(a, b)
        ac = a*c // math.gcd(a, c)
        bc = b*c // math.gcd(b, c)
        abc = a*bc // math.gcd(a, bc)
        
        left, right = 1, n*min(a, b, c)
        
        while left < right:
            mid = left + (right - left) // 2
            if isdiv(mid):
                right = mid
            else:
                left = mid + 1
        
        return left