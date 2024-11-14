class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(num):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / num)
            return stores <= n
        
        l, r = 1, max(quantities)
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return res