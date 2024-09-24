class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        
        for val in range(len(arr), 1, -1):
            i = arr.index(val)
            res.extend([i+1, val])
            arr = arr[i+1:][::-1] + arr[:i]
        
        return res