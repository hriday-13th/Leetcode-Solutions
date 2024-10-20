MAX = 10 ** 6 + 1

primes = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2
    
for i in range(3, MAX, 2):
    if not primes[i]:
        sp[i] = i
        j = i
        while i * j < MAX:
            if not primes[i*j]:
                primes[i*j] = True
                sp[i*j] = i
            j += 2
            
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.reverse()
        res = 0
        
        for i in range(1, len(nums)):
            while nums[i] > nums[i-1]:
                if nums[i] == sp[nums[i]]:
                    return -1
                nums[i] = sp[nums[i]]
                res += 1
                
        return res