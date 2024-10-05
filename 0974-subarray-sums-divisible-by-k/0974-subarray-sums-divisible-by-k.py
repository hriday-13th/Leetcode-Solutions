class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        
        arr = [1] + [0] * k
        
        for i in nums:
            prefix = (prefix + i) % k
            res += arr[prefix]
            arr[prefix] += 1
            
        return res