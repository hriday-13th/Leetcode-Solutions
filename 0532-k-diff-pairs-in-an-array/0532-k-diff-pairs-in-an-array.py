class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        
        res = 0
        
        for i in cnt:
            if (k > 0 and i + k in cnt) or (k == 0 and cnt[i] > 1):
                res += 1
                
        return res