class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        
        heap = []
        
        for i, ele in enumerate(nums):
            heapq.heappush(heap, (ele, i))
            
        seen = set()
        
        while heap:
            val, ind = heapq.heappop(heap)
            if ind not in seen:
                seen.add(ind - 1)
                seen.add(ind)
                seen.add(ind + 1)
                res += val
                
        return res