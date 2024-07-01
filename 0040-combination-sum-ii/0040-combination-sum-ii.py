class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         res = []

#         def backtrack(ind, curr, total):
#             if total == target:
#                 res.append(list(curr))  # Copy the current list to avoid reference issues
#                 return
#             if total > target or ind >= len(candidates):
#                 return

#             for i in range(ind, len(candidates)):
#                 if i > ind and candidates[i] == candidates[i - 1]:  # Skip duplicates
#                     continue
#                 curr.append(candidates[i])
#                 backtrack(i + 1, curr, total + candidates[i])
#                 curr.pop()

#         backtrack(0, [], 0)
#         return res
        candidates.sort()
        res = []
        
        def backtrack(ind, curr, total):
            if total == target:
                res.append(list(curr))
                return
            if total > target or ind >= len(candidates):
                return
            
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return res