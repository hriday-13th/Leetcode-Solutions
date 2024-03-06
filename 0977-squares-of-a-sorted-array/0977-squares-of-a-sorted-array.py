class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [i*i for i in nums]
        return sorted(l)