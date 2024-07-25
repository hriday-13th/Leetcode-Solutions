class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)
        return self.merger(left_sorted, right_sorted)
    
    def merger(self, arr1, arr2):
        lis = []
        i, j = 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                lis.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                lis.append(arr2[j])
                j += 1
                
        lis.extend(arr1[i:])
        lis.extend(arr2[j:])
        
        return lis