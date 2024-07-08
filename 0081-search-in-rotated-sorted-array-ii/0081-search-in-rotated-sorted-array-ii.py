class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            
            if nums[low] == nums[mid]:
                low += 1
                continue
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
#         left, right = 0, len(nums) - 1
        
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return True
            
#             if nums[left] == nums[mid]:
#                 left += 1
#                 continue
                
#             if nums[left] < nums[right]:
#                 if nums[left] <= target and target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
                    
#             else:
#                 if nums[mid] < target and target < nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid + 1
                    
#         return False