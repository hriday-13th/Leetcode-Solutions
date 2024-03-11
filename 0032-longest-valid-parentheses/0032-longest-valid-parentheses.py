class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        l = [0] * n
        stack = []
        
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")" and stack:
                l[stack.pop()] = 1
                l[i] = 1
        
        ans, temp = 0, 0
        
        for i in l:
            if i == 1:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0
                
        return ans