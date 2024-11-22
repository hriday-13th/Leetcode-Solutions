class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = {}
        
        for row in matrix:
            norm = tuple(ele if row[0] == 0 else 1 - ele for ele in row)
            count[norm] = count.get(norm, 0) + 1
            
        return max(count.values())