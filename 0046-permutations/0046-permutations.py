class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            p = self.permute(nums)
            
            for j in p:
                j.append(n)
            res.extend(p)
            nums.append(n)
            
        return res