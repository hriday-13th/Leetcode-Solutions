class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = nums[0] % 2
        odd, even, both = 0, 0, 0
        
        for i in nums:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
                
            if i % 2 == c:
                both += 1
                c = 1 - c
                
        return max(odd, even, both)