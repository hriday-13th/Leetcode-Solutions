class Solution(object):
    def diffWaysToCompute(self, expr):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(expr)):
            op = expr[i]
            
            if op in "+-*":
                s1 = self.diffWaysToCompute(expr[:i])
                s2 = self.diffWaysToCompute(expr[i+1:])
                
                for val1 in s1:
                    for val2 in s2:
                        if op == "+":
                            res.append(int(val1) + int(val2))
                        if op == "-":
                            res.append(int(val1) - int(val2))
                        if op == "*":
                            res.append(int(val1) * int(val2))
                            
        if len(res) == 0:
            res.append(int(expr))
            
        return res