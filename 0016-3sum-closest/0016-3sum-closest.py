class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float('inf')

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s

        return closest