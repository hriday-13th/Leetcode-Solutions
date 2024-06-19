class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                t = seen[nums[i]]
                if i - t <= k:
                    return True
                seen[nums[i]] = i
                
        return False