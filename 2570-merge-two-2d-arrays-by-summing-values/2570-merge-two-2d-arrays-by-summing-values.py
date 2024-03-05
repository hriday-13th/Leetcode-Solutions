class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        w = sorted(nums1 + nums2, key=lambda x : x[0])
        i = 0
        while i < len(w) - 1:
            if w[i][0] == w[i+1][0]:
                w[i][1] = w[i][1] + w[i+1][1]
                w.pop(i+1)
            i += 1
        return w