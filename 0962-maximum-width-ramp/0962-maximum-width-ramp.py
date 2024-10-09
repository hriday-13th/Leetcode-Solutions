class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        res = 0
        
        for i, val in enumerate(nums):
            if not st or nums[st[-1]] > val:
                st.append(i)
                
        for j in range(len(nums))[::-1]:
            while st and nums[st[-1]] <= nums[j]:
                res = max(res, j - st.pop())
                
        return res