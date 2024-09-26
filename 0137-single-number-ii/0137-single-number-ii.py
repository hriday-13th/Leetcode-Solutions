class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = defaultdict(int)
        
        for i in nums:
            if i not in h:
                h[i] = 0
            h[i] += 1
            
        for i in h:
            if h[i] < 3:
                return i