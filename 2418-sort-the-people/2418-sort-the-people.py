class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dct = dict(zip(heights, names))
        d = dict(sorted(dct.items()))
        
        return list(d.values())[::-1]