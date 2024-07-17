class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        k = (num - 3) / 3
        
        if k.is_integer():
            k = int(k)
            return [k, k + 1, k + 2]
        else:
            return []