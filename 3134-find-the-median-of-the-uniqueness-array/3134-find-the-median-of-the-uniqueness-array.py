class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def count(val):
            count = defaultdict(int)
            l = 0
            res = 0
            
            for r in range(len(nums)):
                count[nums[r]] += 1
                
                while len(count) > val:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        count.pop(nums[l])
                    l += 1
                    
                res += r - l + 1
            return res
        
        l, r = 0, len(set(nums))
        n = len(nums)
        med = n * (n + 1) // 2
        while l < r:
            mid = (l + r) // 2
            if count(mid) * 2 >= med:
                r = mid
            else:
                l = mid + 1
                
        return l