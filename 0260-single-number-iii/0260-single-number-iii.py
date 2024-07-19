class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
            
        diff_bit = xor & -xor
        
        n1, n2 = 0, 0
        for num in nums:
            if num & diff_bit:
                n1 ^= num
            else:
                n2 ^= num
                
        return [n1, n2]