class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def reducer(s):
            stack = deque()
            for i in s:
                if i == "#":
                    if stack:
                        stack.pop()
                    else:
                        continue
                else:
                    stack.append(i)
            return "".join(stack)
        
        return reducer(s) == reducer(t)