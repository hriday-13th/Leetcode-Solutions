class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele = sum(nums)
        dig = 0
        
        for i in nums:
            while i > 0:
                dig += i % 10
                i //= 10
                
        return abs(ele - dig)