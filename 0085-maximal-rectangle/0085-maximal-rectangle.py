class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        
        ls = [0] * cols
        
        for r in range(rows):
            st = []
            for i in range(cols):
                if matrix[r][i] == "0":
                    ls[i] = 0
                else:
                    ls[i] += 1
            
            for i, h in enumerate(ls):
                val = i
                while st and st[-1][1] > h:
                    pop_i, pop_ht = st.pop()
                    res = max(res, pop_ht * (i - pop_i))
                    val = pop_i
                st.append([val,h])
                
            while st:
                pop_i, pop_ht = st.pop()
                res = max(res, pop_ht * (cols - pop_i))
                
        return res