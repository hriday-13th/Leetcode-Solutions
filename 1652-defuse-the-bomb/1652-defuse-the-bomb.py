class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            l = [0] * n
            return l
        
        elif k > 0:
            res = []
            for i in range(n):
                s = 0
                for j in range(i+1, i+k+1):
                    s += code[j % n]
                res.append(s)
            
        elif k < 0:
            res = []
            for i in range(n):
                s = 0
                for j in range(i-1, i+k-1, -1):
                    s += code[j % n]
                res.append(s)
            
        return res