class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        res = []
        
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
                
        return res