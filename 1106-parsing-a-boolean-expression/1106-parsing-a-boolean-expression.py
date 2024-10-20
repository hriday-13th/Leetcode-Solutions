class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for i in expression:
            if i != ")":
                stack.append(i)
            elif i == ",":
                continue
            else:
                count_t, count_f = 0, 0
                
                while stack and stack[-1] != "(":
                    c = stack.pop()
                    if c == "f":
                        count_f += 1
                    if c == "t":
                        count_t += 1
                        
                stack.pop()
                op = stack.pop()
                curr_ex = "f"
                
                if op == "|":
                    curr_ex = "t" if count_t > 0 else "f"
                elif op == "&":
                    curr_ex = "t" if count_t > 0 and count_f == 0 else "f"
                elif op == "!":
                    curr_ex = "f" if count_t == 1 else "t"
                    
                stack.append(curr_ex)
                
                
        return True if stack[0] == "t" else False