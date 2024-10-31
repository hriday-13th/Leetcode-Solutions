class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def foo(arr):
            dp = [float('inf')] * (len(arr) + 1)
            l = [0] * len(arr)
            for i, ele in enumerate(arr):
                l[i] = bisect_left(dp, ele) + 1
                dp[l[i] - 1] = ele
            return l
        
        l1, l2 = foo(nums), foo(nums[::-1])[::-1]
        res, n = 0, len(nums)
        
        for i in range(n):
            if l1[i] > 1 and l2[i] > 1:
                res = max(res, l1[i] + l2[i] - 1)
                
        return n - res