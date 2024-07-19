class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        for i in range(rows):
            min_val = min(matrix[i])
            min_index = matrix[i].index(min_val)

            is_lucky = True
            for j in range(rows):
                if matrix[j][min_index] > min_val:
                    is_lucky = False
                    break

            if is_lucky:
                res.append(min_val)

        return res
#         rows = len(matrix)
#         cols = len(matrix[0])
        
#         res = []
        
#         for i in range(rows):
#             min_val = min(matrix[i])
#             ind = matrix[i].index(min_val)
            
#             lucky = True
            
#             for j in range(cols):
#                 if matrix[j][ind] > min_val:
#                     lucky = False
#                     break
                    
#             if lucky:
#                 res.append(min_val)
            
#         return res