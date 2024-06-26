class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return[-1, -1]
        
        l, h = 0, len(nums) - 1
    
        def first(nums, target, l, r):
            pos = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    pos = mid
            return pos
        
        def last(nums, target, l, r):
            pos = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    pos = mid
            return pos
        
        
        a = first(nums, target, l, h)
        b = last(nums, target, l, h)
        return [a,b]