class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] in row[i] or matrix[i][j] in col[j]:
                    return False
                row[i].add(matrix[i][j])
                col[j].add(matrix[i][j])
                
        return True