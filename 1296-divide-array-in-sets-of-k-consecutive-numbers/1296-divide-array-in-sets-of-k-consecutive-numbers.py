class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        start = deque()
        last, opened = -1, 0
        
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last + 1:
                return False
            start.append(c[i] - opened)
            last, opened = i, c[i]
            if len(start) == k:
                opened -= start.popleft()
                
        return opened == 0