class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        if n == 1:
            return queries[-1][-1]
        
        rows = [(0, 0)] * n
        cols = [(0, 0)] * n
        
        for i in range(len(queries)):
            if queries[i][0] == 0:
                rows[queries[i][1]] = (i+1, queries[i][2])
            elif queries[i][0] == 1:
                cols[queries[i][1]] = (i+1, queries[i][2])
                
        rows.sort(key=lambda x: x[0], reverse=True)
        cols.sort(key=lambda x: x[0], reverse=True)
        
        res = 0
        i, j = 0, 0
        col_val, row_val = n, n
        
        while i < n and j < n:
            if rows[i][0] > cols[j][0]:
                res += rows[i][1] * row_val
                col_val -= 1
                i += 1
            else:
                res += cols[j][1] * col_val
                row_val -= 1
                j += 1
                
        while i < n:
            res += rows[i][1] * row_val
            col_val -= 1
            i += 1
            
        while j < n:
            res += cols[j][1] * col_val
            row_val -= 1
            j += 1
            
        return res