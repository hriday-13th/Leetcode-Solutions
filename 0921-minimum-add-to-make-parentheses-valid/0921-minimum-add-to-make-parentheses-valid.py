class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for i in s:
            if not stack or i == "(":
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
                
        return len(stack)