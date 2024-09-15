class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        
        for i, k in c.items():
            if k == 2:
                res.append(i)
                
        return res