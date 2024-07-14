class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [{}]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == "(":
                stack.append({})
                i += 1
            elif formula[i] == ")":
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mul = int(formula[start : i] or 1)
                for element, count in top.items():
                    stack[-1][element] = stack[-1].get(element, 0) + count * mul
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start : i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start : i] or 1)
                stack[-1][element] = stack[-1].get(element, 0) + count
                
        res = stack.pop()
        sorted_res = sorted(res.keys())
        
        ans = ""
        for i in sorted_res:
            ans += i
            ans += str(res[i]) if res[i] > 1 else ''
            
        return ans