class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        
        for i, h in enumerate(heights):
            curr = i
            
            while stack and stack[-1][1] > h:
                pop_i, pop_ht = stack.pop()
                res = max(res, pop_ht * (i - pop_i))
                curr = pop_i
            stack.append([curr, h])
        
        while stack:
            idx, he = stack.pop()
            res = max(res, (len(heights) - idx) * he)
        
        return res