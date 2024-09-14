class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [nums]
        
        for i in range(len(nums)):
            res.extend(list(itertools.combinations(nums, i)))
            
        return res