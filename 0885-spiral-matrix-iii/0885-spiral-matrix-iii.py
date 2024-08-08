class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[rStart, cStart]]
        steps = 0
        total = rows * cols
        d = 0
        
        while len(res) < total:
            if d % 2 == 0:
                steps += 1
                
            for _ in range(steps):
                rStart += directions[d][0]
                cStart += directions[d][1]
                
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    if len(res) == total:
                        return res
                    
            d = (d + 1) % 4
                
        return res