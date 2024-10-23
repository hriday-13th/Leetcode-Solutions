class Solution(object):
    def findPeakGrid(self, mat):
        rows, cols = len(mat), len(mat[0])
        start, end = 0, cols - 1
        
        while start <= end:
            row1 = 0
            mid = (start + end) // 2
            
            for row2 in range(rows):
                row1 = row2 if (mat[row2][mid] >= mat[row1][mid]) else row1
                
            is_left = mid - 1 >= start and mat[row1][mid - 1] > mat[row1][mid]
            is_right = mid + 1 <= end and mat[row1][mid + 1] > mat[row1][mid]
            
            if not is_left and not is_right:
                return [row1, mid]
            elif is_right:
                start = mid + 1
            else:
                end = mid - 1
            
        return []