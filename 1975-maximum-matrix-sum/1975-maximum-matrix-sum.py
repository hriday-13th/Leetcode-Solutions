class Solution(object):
    def maxMatrixSum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        
        net_sum = 0
        neg_count = 0
        lowest_neg = float('inf')
        
        for i in range(rows):
            for j in range(cols):
                net_sum += abs(matrix[i][j])
                lowest_neg = min(lowest_neg, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    neg_count += 1
                    
        if neg_count % 2 == 0:
            return net_sum
        return net_sum - 2 * lowest_neg