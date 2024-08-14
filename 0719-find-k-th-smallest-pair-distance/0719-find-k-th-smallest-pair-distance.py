class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1]
        
        def pairings(val):
            count = 0
            l = 0
            
            for r in range(1, len(nums)):
                while nums[r] - nums[l] > val and l < r:
                    l += 1
                    
                if nums[r] - nums[l] <= val:
                    count += (r - l)
                    
            return count
        
        while l <= r:
            mid = (l + r) // 2
            ans = pairings(mid)
            if ans >= k:
                if pairings(mid - 1) < k:
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
                
        