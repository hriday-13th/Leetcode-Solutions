class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        tab = {}
        res = []
        
        for arr in nums:
            for i in arr:
                tab[i] = tab.get(i, 0) + 1
                
        for ele in tab:
            if tab[ele] == len(nums):
                res.append(ele)
                
        return sorted(res)