class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        
        for i in nums:
            if i > 9:
                double_sum += i
            else:
                single_sum += i
                
        return single_sum != double_sum