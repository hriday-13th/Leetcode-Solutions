class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        res = set()
        while i < len(nums1) and j < len(nums2):
            x, y = nums1[i], nums2[j]
            if x == y:
                res.add(x)
                i += 1
                j += 1
            elif x < y:
                i += 1
            else:
                j += 1
                
        return list(res)