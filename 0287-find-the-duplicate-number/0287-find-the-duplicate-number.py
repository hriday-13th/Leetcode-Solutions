class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sorted(nums)
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return s[i]