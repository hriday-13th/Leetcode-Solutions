class Solution(object):
    def maxKelements(self, nums, k):
        max_heap = [-num for num in nums]
        heapify(max_heap)
        res = 0
        
        for i in range(k):
            res -= max_heap[0]
            heapreplace(max_heap, max_heap[0] // 3)
            
        return res