class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        pairs = 0

        def finder(target, end):
            l, r = 0, end
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        for i in range(len(nums)):
            a = finder(lower - nums[i], i)
            b = finder(upper - nums[i] + 1, i)
            pairs += b - a

        return pairs