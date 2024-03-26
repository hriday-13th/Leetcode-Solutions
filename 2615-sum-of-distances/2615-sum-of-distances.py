class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = {}
        left = [0] * len(nums)
        right = [0] * len(nums)
        res = []
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i, 1]
            else:
                left[i] = abs(i - d[nums[i]][0]) * d[nums[i]][1] + left[d[nums[i]][0]]
                d[nums[i]][0] = i
                d[nums[i]][1] += 1
        
        d = {}
        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in d:
                d[nums[i]] = [i, 1]
            else:
                right[i] = abs(i - d[nums[i]][0]) * d[nums[i]][1] + right[d[nums[i]][0]]
                d[nums[i]][0] = i
                d[nums[i]][1] += 1
        
        for a,b in zip(left, right):
            temp = a+b
            res += [temp]
            
        return res