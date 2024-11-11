primes = [True] * 1001

primes[0] = primes[1] = False
prev_prime = 0

for i in range(2, 1001):
    if primes[i]:
        prev_prime = i
        for j in range(i*i, 1001, i):
            primes[j] = False
        
class Solution(object):
    def primeSubOperation(self, nums):
        prev = 0
        
        for num in nums:
            if prev >= num:
                return False
            for p in range(num - 1, -1, -1):
                if primes[p] and num - p > prev:
                    break
            prev = num - p
            
        return True