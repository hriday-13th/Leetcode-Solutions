class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        lis = [i+1 for i in range(n**2)]
        res = [[0] * n for i in range(n)]
        
        r1, r2 = 0, n-1
        c1, c2 = 0, n-1
            
        while lis:
            for i in range(c1,c2+1):
                if not lis:
                    break
                res[r1][i] = lis[0]
                lis.pop(0)  
            r1 += 1
            
            for j in range(r1, r2+1):
                if not lis:
                    break
                res[j][c2] = lis[0]
                lis.pop(0)
            c2 -= 1
            
            if r1 <= r2:
                for i in range(c2, c1-1, -1):
                    if not lis:
                        break
                    res[r2][i] = lis[0]
                    lis.pop(0)
                r2 -= 1
                
            if c1 <= c2:
                for j in range(r2, r1-1, -1):
                    if not lis:
                        break
                    res[j][c1] = lis[0]
                    lis.pop(0)
                c1 += 1

        return res