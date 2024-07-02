class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d = collections.defaultdict()
        arr1, arr2 = [], []
        
        for i in nums1:
            if i not in d:
                d[i] = [True, False]
                
        for j in nums2:
            if j in d:
                d[j][1] = True
            else:
                d[j] = [False, True]
                
        for ele in d:
            if d[ele][0] and not d[ele][1]:
                arr1.append(ele)
            if d[ele][1] and not d[ele][0]:
                arr2.append(ele)
                
        return [arr1, arr2]