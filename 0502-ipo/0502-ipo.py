class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prof = []
        cap = [(a,b) for a, b in zip(capital, profits)]
        heapq.heapify(cap)
        
        for i in range(k):
            while cap and cap[0][0] <= w:
                c, p = heapq.heappop(cap)
                heapq.heappush(prof, -1 * p)
            if not prof:
                break
            w += -1 * heapq.heappop(prof)
            
        return w