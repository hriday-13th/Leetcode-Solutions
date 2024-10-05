class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        num = 0
        
        for i in word:
            num = num * 10 + int(i)
            
            if num % m:
                res.append(0)
            else:
                res.append(1)
                
            num %= m
            
        return res