class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = []
        flag = True
        for index, ele in enumerate(nums):
            if ele == 1:
                l += [index]
                
        for i in range(len(l) - 1):
            if l[i+1] - l[i] < k+1:
                flag = False
            else:
                continue
                
        return flag