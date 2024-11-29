class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')
        curr_sum = 0
        min_heap = []
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= k:
                res = min(res, r + 1)
            while min_heap and curr_sum - min_heap[0][0] >= k:
                prefix, end_idx = heapq.heappop(min_heap)
                res = min(res, r - end_idx)
            heapq.heappush(min_heap, (curr_sum, r))
            
        return -1 if res == float('inf') else res