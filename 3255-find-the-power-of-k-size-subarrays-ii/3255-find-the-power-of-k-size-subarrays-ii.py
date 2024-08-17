class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        a = 1
        pre = [1]
        
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                a += 1
                pre.append(a)
            else:
                a = 1
                pre.append(a)
                
        for i in range(len(nums) - k + 1):
            if (pre[i + k - 1] - pre[i] + 1) == k:
                res.append(nums[i + k - 1])
            else:
                res.append(-1)
                
        return res