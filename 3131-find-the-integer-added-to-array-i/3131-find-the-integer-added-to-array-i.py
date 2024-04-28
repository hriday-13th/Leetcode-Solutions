class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        ls1 = sorted(nums1)
        ls2 = sorted(nums2)
        
        return ls2[0] - ls1[0]
#         diff = 0
#         for a,b in zip(ls1, ls2):
#             diff = b-a
            
#         return diff