class Solution:
    def getMaximumXor(self, nums: List[int], bit: int) -> List[int]:
        curr = 0
        res = []
        mask = (1 << bit) - 1
        
        for i in nums:
            curr ^= i
            res.append(curr ^ mask)
            
        return res[::-1]