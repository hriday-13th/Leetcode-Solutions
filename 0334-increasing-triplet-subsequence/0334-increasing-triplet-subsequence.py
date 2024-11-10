class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fst = sec = float('inf')
        
        for i in nums:
            if i <= fst:
                fst = i
            elif i <= sec:
                sec = i
            else:
                return True
            
        return False