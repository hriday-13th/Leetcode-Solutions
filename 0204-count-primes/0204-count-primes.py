class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1] * n
        
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] == 1:
                for j in range(i*i, n, i):
                    prime[j] = 0
                    
        res = 0
        for i in range(2, n):
            if prime[i] == 1:
                res += 1
                
        return res