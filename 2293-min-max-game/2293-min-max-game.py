class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            new_nums = []
            n = len(nums)
            for i in range(0,n,2):
                a = nums[i]
                b = nums[i+1]
                
                p = i // 2
                
                if p%2 == 0:
                    new_nums.append(min(a,b))
                else:
                    new_nums.append(max(a,b))
            nums = new_nums
        return nums[0]