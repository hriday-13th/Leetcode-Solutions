class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        d = defaultdict(int)
        nums.sort(reverse = True)
        
        for i in nums:
            if i ** 2 not in d:
                d[i] = -1
            else:
                d[i] = i ** 2
        
        count = -1
        for i in d.keys():
            curr = 1
            while d[i] != -1:
                curr += 1
                i = d[i]
            if curr != 1:
                count = max(count, curr)
                
        return count