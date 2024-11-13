class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n // k < 2:
            return False
        if k == 1:
            return True
        
        visited = [0] * n
        l, r = 0, 1
        
        while r < n:
            while r < n and nums[r] > nums[r-1]:
                if r - l + 1 == k:
                    visited[l] = 1
                    l += 1
                r += 1
            l = r
            r += 1
            
        for i in range(n - 2*k + 1):
            if visited[i] and visited[i + k]:
                return True
            
        return False