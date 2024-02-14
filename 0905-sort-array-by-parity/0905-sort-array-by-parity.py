class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        eve = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2 != 0]
        
        return eve + odd