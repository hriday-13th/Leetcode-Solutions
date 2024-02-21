class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(" : ")", "[" : "]", "{" : "}"}
        
        l = list(s)
        stack = []
        
        for char in l:
            if char in d.keys():
                stack.append(char)
            elif stack and char == d[stack[-1]]:
                    stack.pop(-1)
            else:
                return False
            
        return not stack