class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        
        @cache
        def helper(num):
            count = 0
            for n in nums:
                count +=  (n - 1) // num
                if count > maxOperations:
                    break
            return count
        
        l, r = 1, nums[-1]
        
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid) <= maxOperations:
                r = mid - 1
            else:
                l = mid + 1
                
        return l