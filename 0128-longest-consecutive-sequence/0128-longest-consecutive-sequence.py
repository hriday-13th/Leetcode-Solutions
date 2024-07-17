class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in nums:
                curr = num
                curr_streak = 1
                
                while curr + 1 in nums:
                    curr_streak += 1
                    curr += 1
                    
                res = max(res, curr_streak)
                
        return res