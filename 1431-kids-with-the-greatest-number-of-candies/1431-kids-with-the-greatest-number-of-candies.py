class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        
        l = [True if i + extraCandies >= m else False for i in candies]
        return l