class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        val = 0
        even, odd = 1, 0
        
        for i in arr:
            val += i
            
            if val % 2 == 0:
                even += 1
            else:
                odd += 1
                
        return (even * odd) % 1000000007