class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
                
        res = []
        backtrack(0, [])
        return res
#         res = [nums]
        
#         for i in range(len(nums)):
#             res.extend(list(itertools.combinations(nums, i)))
            
#         return res