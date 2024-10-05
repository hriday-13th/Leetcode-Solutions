class Solution:
    def minMoves(self, nums: List[int]) -> int:
        val = min(nums)
        res = 0
        
        for x in nums:
            res += x - val
        
        return res