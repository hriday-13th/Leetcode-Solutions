class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()
        
        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][0] > temp:
                stack.append([temp, i])
            else:
                while stack and temp > stack[-1][0]:
                    pop_temp, pop_i = stack.pop()
                    res[pop_i] = i - pop_i
                stack.append([temp, i])
            
        return res