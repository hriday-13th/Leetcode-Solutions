class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        minheap = []
        
        for i in range(1, n+1):
            for j in range(i):
                heapq.heappush(minheap, prefix[i] - prefix[j])
                
        res = 0
        for i in range(1, right + 1):
            val = heapq.heappop(minheap)
            if i >= left:
                res = (res + val) % 1000000007
                
        return res