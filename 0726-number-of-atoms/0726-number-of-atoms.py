class Solution:
    def countOfAtoms(self, formula: str) -> str:
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
                for element, atoms in top.items():
                    stack[-1][element] = stack[-1].get(element, 0) + atoms * mul
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start : i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                atoms = int(formula[start : i] or 1)
                stack[-1][element] = stack[-1].get(element, 0) + atoms
                
        elements = stack.pop()
        sort_elements = sorted(elements.keys())
        
        ans = ""
        for i in sort_elements:
            ans += i
            ans += str(elements[i]) if elements[i] > 1 else ''
            
        return ans