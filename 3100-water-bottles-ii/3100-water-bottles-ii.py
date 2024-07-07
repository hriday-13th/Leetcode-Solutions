class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        ans = b
        
        while b >= e:
            ans += 1
            b = b - e + 1
            e += 1
            
        return ans