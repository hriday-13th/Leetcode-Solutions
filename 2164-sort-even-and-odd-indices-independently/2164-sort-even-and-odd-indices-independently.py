from itertools import zip_longest
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        pos = sorted([nums[i] for i in range(0,len(nums),2)])
        neg = sorted([nums[i] for i in range(1,len(nums),2)], reverse = True)
        res = []
        for a,b in zip_longest(pos,neg,fillvalue=None):
            if a is not None:
                res.append(a)
            if b is not None:
                res.append(b)
        return res