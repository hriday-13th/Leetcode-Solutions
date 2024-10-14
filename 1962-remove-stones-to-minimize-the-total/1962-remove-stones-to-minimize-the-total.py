class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-x for x in piles]
        heapify(max_heap)
        res = 0
        
        for i in range(k):
            val = -max_heap[0] // 2
            res += val
            heapreplace(max_heap, max_heap[0] + val)
            
        return sum(piles) - res