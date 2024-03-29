class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1 or b == 0:
            return 1
        
        num = ''
        for i in b:
            num += str(i)
            
        num = int(num)
        return pow(a, num, 1337)