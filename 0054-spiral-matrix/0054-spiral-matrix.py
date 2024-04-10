class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1
        net = (r2+1)*(c2+1)
        ans = []
        
        while len(ans) < net:
            for i in range(c1,c2+1):
                ans.append(matrix[r1][i])
            r1 += 1
            for j in range(r1, r2+1):
                ans.append(matrix[j][c2])
            c2 -= 1
            if r1 <= r2:
                for i in range(c2, c1-1, -1):
                    ans.append(matrix[r2][i])
                r2 -= 1
            if c1 <= c2:
                for j in range(r2, r1-1, -1):
                    ans.append(matrix[j][c1])
                c1 += 1
            
        return ans