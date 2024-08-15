class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        h = []
        
        for i in range(rows):
            for j in range(cols):
                heapq.heappush(h, -matrix[i][j])
                if len(h) > k:
                    heapq.heappop(h)
                    
        return -heapq.heappop(h)