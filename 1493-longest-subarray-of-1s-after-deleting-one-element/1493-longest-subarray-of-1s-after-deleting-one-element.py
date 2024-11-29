class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        prev = 0
        curr = 0
        
        for i in nums:
            if i == 1:
                curr += 1
            else:
                if prev == 0:
                    arr.append(0)
                else:
                    arr.append(curr)
                    curr = 0
            prev = i
        arr.append(curr)
        
        if len(arr) == 1:
            return arr[0] - 1
        
        res = 0
        for i in range(len(arr) - 1):
            res = max(res, arr[i] + arr[i + 1])
            
        return res