class Solution(object):
    def findSubsequences(self, nums):
        res = []
        
        def helper(ind, path):
            if len(path) > 1:
                res.append(path[:])
            
            seen = set()
            for i in range(ind, len(nums)):
                if nums[i] in seen:
                    continue
                if not path or nums[i] >= path[-1]:
                    seen.add(nums[i])
                    helper(i + 1, path + [nums[i]])
        
        helper(0, [])
        return res