class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = max(nums)
        l = len(nums)
        left = 0
        freq = 0
        count = 0
        
        for right in range(l):
            if nums[right] == n:
                freq += 1
            while left < right and freq >= k:
                # print(nums[left:right+1])
                count += l - right
                if nums[left] == n:
                    freq -= 1
                left += 1
            if freq == k:
                count += 1
            
        return count