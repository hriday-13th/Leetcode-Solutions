class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pre = [0]
        was_even = nums[0] % 2 == 0
        
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0 ^ was_even:
                pre.append(pre[-1] + 1)
            else:
                pre.append(pre[-1])
            was_even = nums[i] % 2 == 0
                
        res = []
        for i, j in queries:
            if pre[j] - pre[i] == j - i:
                res.append(True)
            else:
                res.append(False)
                
        return res