class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num, max_idx = -1, -1
        second_max_num = -1
        
        for i in range(len(nums)):
            if nums[i] > max_num:
                second_max_num = max_num
                max_num = nums[i]
                max_idx = i
            elif nums[i] > second_max_num:
                second_max_num = nums[i]
                
        return max_idx if max_num >= 2 * second_max_num else -1