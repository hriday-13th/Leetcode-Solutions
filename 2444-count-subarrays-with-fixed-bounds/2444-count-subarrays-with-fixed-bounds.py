class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_i, max_i = -1, -1
        left, right = -1, 0
        res = 0
        
        while right < len(nums):
            if nums[right] < minK or nums[right] > maxK:
                min_i = right
                max_i = right
                left = right
                
            min_i = right if nums[right] == minK else min_i
            max_i = right if nums[right] == maxK else max_i
            
            res += min(max_i, min_i) - left
            right += 1
            
        return res
#         res = 0
#         i = 0
        
#         while i < len(nums):
#             if nums[i] not in range(minK, maxK + 1):
#                 i += 1
#             else:
#                 count_min, count_max = 0, 0
#                 left = i
                
#                 if nums[i] == minK:
#                     count_min += 1
#                 if nums[i] == maxK:
#                     count_max += 1
                    
#                 while i+1 < len(nums) and nums[i+1] in range(minK, maxK + 1):
#                     if nums[i+1] == minK:
#                         count_min += 1
#                     elif nums[i+1] == maxK:
#                         count_max += 1
#                     i += 1
                
#                 if count_min == 0 or count_max == 0:
#                     continue
                    
#                 else:
#                     while left < i and count_min > 0 and count_max > 0:
#                         res += 1
#                         if nums[left] == minK:
#                             count_min -= 1
#                         elif nums[left] == maxK:
#                             count_max -= 1
#                         left += 1
#                     i += 1
                        
#         return res