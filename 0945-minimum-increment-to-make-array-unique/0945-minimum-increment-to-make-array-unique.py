from collections import Counter
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        new = nums[0]
        count = 0
        
        for i in nums:
            new = max(new, i)
            count += new - i
            new += 1
            
        return count