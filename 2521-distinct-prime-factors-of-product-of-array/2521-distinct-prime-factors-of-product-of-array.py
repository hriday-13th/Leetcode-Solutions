from typing import List
from functools import cache

MAX = 10 ** 4 + 1
primes = [True] * MAX
factors = [[] for _ in range(MAX)]

primes[0] = primes[1] = False

for i in range(2, MAX):
    if primes[i]:
        factors[i].append(i)
        for j in range(i * 2, MAX, i):
            factors[j].append(i)
            primes[j] = False

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        count = []
        for num in nums:
            count.extend(factors[num])
        return len(set(count))
