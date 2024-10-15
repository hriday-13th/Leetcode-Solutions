class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        counter = Counter(nums)
        
        def backtrack(res):
            if len(res) == len(nums):
                perms.append(res)
                return
            
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    backtrack(res + [key])
                    counter[key] += 1
        
        backtrack([])
        return perms