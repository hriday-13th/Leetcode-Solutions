class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        startCol = 0
        endCol = len(mat[0]) - 1
        
        while startCol <= endCol:
            maxRow = 0
            midCol = (startCol + endCol) // 2
            
            for row in range(len(mat)):
                maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
                
            is_left = midCol - 1 >= startCol and mat[maxRow][midCol - 1] > mat[maxRow][midCol]
            is_right = midCol + 1 <= endCol and mat[maxRow][midCol] < mat[maxRow][midCol + 1]
            
            if not is_left and not is_right:
                return [maxRow, midCol]
            elif is_right:
                startCol = midCol + 1
            else:
                endCol = midCol - 1
            
        return []