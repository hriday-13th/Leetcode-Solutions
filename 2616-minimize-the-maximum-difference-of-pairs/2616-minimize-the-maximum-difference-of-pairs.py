class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        def calc(val):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= val:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count
            
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        
        while l < r:
            mid = (l + r) // 2
            if calc(mid) >= p:
                r = mid
            else:
                l = mid + 1
                
        return l