class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        def lis(arr):
            arr.sort(key=lambda t : (t[0], -t[1]))
            res = []
            
            for x, y in arr:
                if not res or y > res[-1]:
                    res.append(y)
                else:
                    i = bisect_left(res, y)
                    res[i] = y
                    
            return len(res)
        
        mx, my = coordinates[k]
        coordinates.sort()
        
        left = [(i, j) for i, j in coordinates if i < mx and j < my]
        right = [(i, j) for i, j in coordinates if i > mx and j > my]
        
        return 1 + lis(left) + lis(right)