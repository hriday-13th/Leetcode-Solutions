class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def helper(i, j):
            diff = (i + 1) / (j + 1) - (i / j)
            return (-diff, (i, j))
        
        heap = []
        numClasses = len(classes)
        
        for i, j in classes:
            heapq.heappush(heap, helper(i, j))
            
        for _ in range(extraStudents):
            diff, val = heapq.heappop(heap)
            tup = helper(val[0] + 1, val[1] + 1)
            heapq.heappush(heap, tup)
            
        avg = 0
        
        while heap:
            _, val = heapq.heappop(heap)
            avg += val[0] / (val[1] * numClasses)
            
        return avg