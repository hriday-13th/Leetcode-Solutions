class Solution(object):
    def numberOfSubarrays(self, nums, k):
        left = 0
        count = 0
        odd_count = 0
        prefix = 0  # Tracks the number of even numbers before the first odd in the current window

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
                prefix = 0  # Reset prefix count when a new odd number is encountered

            while odd_count == k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                prefix += 1
                left += 1

            count += prefix  # Add valid subarrays ending at the current `right`

        return count