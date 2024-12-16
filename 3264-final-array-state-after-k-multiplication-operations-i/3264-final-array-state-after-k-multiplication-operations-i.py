class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        res = nums.copy()
        
        for i, val in enumerate(nums):
            heapq.heappush(heap, (val, i))
            
        for _ in range(k):
            num, ind = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, ind))
            
        while heap:
            num, ind = heapq.heappop(heap)
            res[ind] = num
            
        return res