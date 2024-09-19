class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(i) for i in nums]
        
        def comp(x, y):
            return -1 if x + y > y + x else 1
        
        arr.sort(key=cmp_to_key(comp))
        
        res = "".join(arr)
        return '0' if res[0] == '0' else res