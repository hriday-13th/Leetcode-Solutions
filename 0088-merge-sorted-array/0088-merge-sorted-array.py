class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m)[::-1]:
            nums1[i + n] = nums1[i]
            
        for j in range(n):
            nums1[j] = 0
        
        i, j = n, 0
        curr = 0
        
        while i < m + n and j < n:
            if nums1[i] <= nums2[j]:
                nums1[curr] = nums1[i]
                i += 1
            else:
                nums1[curr] = nums2[j]
                j += 1
            curr += 1
            
        while j < n:
            nums1[curr] = nums2[j]
            curr += 1
            j += 1