class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        res = 0
        
        for i in gain:
            curr += i
            res = max(res, curr)
            
        return res