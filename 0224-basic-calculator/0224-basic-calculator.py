class Solution:
    def calculate(self, s: str) -> int:
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))
        
            num, stack, sign = 0, [], "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
#         if "+" not in s and "-" not in s:
#             return int(s)
            
#         st = []
        
#         def calc(i, j):
#             if j - i == 2:
#                 return int(st[i+1])
            
#             if j - i == 3:
#                 if st[i+1] == "+":
#                     return int(st[i+2])
#                 else:
#                     return -int(st[i+2])
                
#             i += 1
#             a = int(st[i])
#             for x in range(i+1, j, 2):
#                 op = st[x]
#                 b = int(st[x+1])
#                 if op == "+":
#                     a += b
#                 elif op == "-":
#                     a -= b
#             return a
        
#         for i in range(len(s)):
#             if s[i] != " ":
#                 if s[i] != ")":
#                     st.append(s[i])
#                 else:
#                     temp = st.copy()
#                     while temp[-1] != "(":
#                         temp.pop()
#                     temp.pop()
#                     if temp and len(st) - len(temp) < 4:
#                         prev = st.pop()
#                         k = calc(len(temp), len(st))
#                         if (prev == "+" and k > 0) or (prev == "-" and k < 0):
#                             st.append("+")
#                             st.append(k)
#                         else:
#                             st.append("-")
#                             st.append(k)
#                     else:
#                         k = calc(len(temp), len(st))
#                         st = st[:len(temp)] + [k]
                    
#         return calc(-1, len(st))