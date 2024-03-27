class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        return sorted(nums, key=lambda x: (d[x], -x))