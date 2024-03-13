class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = sorted(nums)
        res = set()
        n = len(l)
        
        for i in range(len(l) - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = l[i] + l[j] + l[k]

                if s == 0:
                    res.add((l[i], l[j], l[k]))
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
                    
        return res