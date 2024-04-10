class Solution:
    def isHappy(self, n: int) -> bool:
        s, f = n, n
        
        def cal(num):
            ans = 0

            while num > 0:
                ans += (num%10)**2
                num //= 10

            return ans
        
        while True:
            s = cal(s)
            f = cal(cal(f))

            if s == f:
                break
        
        return s == 1