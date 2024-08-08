class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = [[rStart, cStart]]
        steps = 0
        d = 0
        total = rows * cols
        
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