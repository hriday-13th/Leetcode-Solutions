class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        x = 0
        
        for i in s:
            if i == "[":
                x += 1
            else:
                x -= 1
            res = min(res, x)
            
        return (- res + 1) // 2