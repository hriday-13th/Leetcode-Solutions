class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = -1
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
                
        if ind == -1:
            nums.sort()
            
        for i in range(n-1, -1, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
                
        if ind + 1 != n-1:
            l = nums[ind+1:]
            l.sort()
            nums[ind+1:] = l[:]