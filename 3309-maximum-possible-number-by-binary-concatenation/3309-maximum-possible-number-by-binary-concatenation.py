class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def comp(a, b):
            if a + b > b + a:
                return -1
            return 1
        
        arr = [bin(i)[2:] for i in nums]
        arr.sort(key=cmp_to_key(comp))
        
        res = "".join(arr)
        return int(res, 2)