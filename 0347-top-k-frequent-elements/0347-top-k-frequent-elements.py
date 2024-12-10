class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        
        for i in counter:
            heapq.heappush(heap, (-counter[i], i))
            
        res = []
        for _ in range(k):
            freq, ele = heapq.heappop(heap)
            res.append(ele)
            
        return res