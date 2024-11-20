class Solution(object):
    def resultsArray(self, nums, k):
        arr = []
        prev = None
        
        for i in nums:
            if prev is None:
                prev = i
                arr.append(1)
            else:
                if i == prev + 1:
                    arr.append(arr[-1] + 1)
                else:
                    arr.append(arr[-1] - 1)
            prev = i
            
        res = []
        for i in range(len(nums) - k + 1):
            if arr[i + k - 1] - arr[i] == k - 1:
                res.append(nums[i+k-1])
            else:
                res.append(-1)
                
        return res