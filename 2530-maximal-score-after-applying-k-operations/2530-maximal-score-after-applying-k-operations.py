class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i, ele in enumerate(nums):
            heapq.heappush(max_heap, (-ele, i))
            
        res = 0
        for i in range(k):
            val, i = heapq.heappop(max_heap)
            res += -val
            new_val = math.ceil(-val / 3)
            heapq.heappush(max_heap, (-new_val, i))
            
        return res