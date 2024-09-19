class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        for i in range(len(expression)):
            op = expression[i]
            if op in "+-*":
                s1 = expression[:i]
                s2 = expression[i+1:]
                str1 = self.diffWaysToCompute(s1)
                str2 = self.diffWaysToCompute(s2)
                
                for i in str1:
                    for j in str2:
                        if op == "+":
                            res.append(int(i) + int(j))
                        if op == "-":
                            res.append(int(i) - int(j))
                        if op == "*":
                            res.append(int(i) * int(j))
                            
        if len(res) == 0:
            res.append(int(expression))
            
        return res