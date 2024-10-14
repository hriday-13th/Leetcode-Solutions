class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-x for x in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            new_value = math.floor(largest ** 0.5)
            heapq.heappush(max_heap, -new_value)

        return -sum(max_heap)