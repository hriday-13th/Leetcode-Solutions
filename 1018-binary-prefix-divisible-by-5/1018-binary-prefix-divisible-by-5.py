class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = 0
        
        for i in range(len(nums)):
            curr += nums[i]
            if curr % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            curr <<= 1
        
        return res