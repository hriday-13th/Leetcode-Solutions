class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        heap = []
        
        for start, end, value in events:
            heapq.heappush(heap, (start, True, value))
            heapq.heappush(heap, (end + 1, False, value))
            
        res = 0
        val = 0
        
        while heap:
            _, is_start, v = heapq.heappop(heap)
            if is_start:
                res = max(res, val + v)
            else:
                val = max(val, v)
                
        return res