from functools import cache

MAX = 10 ** 5 + 1

primes = [True] * MAX
vals = [[] for _ in range(MAX)]
primes[0] = primes[1] = False

for i in range(2, MAX):
    if primes[i]:
        for j in range(2 * i, MAX, i):
            vals[j].append(i)
            primes[j] = False
            
class Solution:
    @cache
    def smallestValue(self, n: int) -> int:
        if primes[n]:
            return n
        
        while not primes[n]:
            temp = n
            curr = 0
            for i in vals[n]:
                while n % i == 0:
                    curr += i
                    n //= i
            if curr == temp:
                return curr
            n = self.smallestValue(curr)
            
        return n