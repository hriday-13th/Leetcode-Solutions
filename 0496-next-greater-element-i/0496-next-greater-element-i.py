class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            ind = nums2.index(i)

            while ind != len(nums2):
                if nums2[ind] <= i:
                    ind += 1
                else:
                    break
            if ind == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[ind])
                
        return res