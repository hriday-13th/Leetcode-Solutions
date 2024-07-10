class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        
        for i in logs:
            if i == "../" and res > 0:
                res -= 1
            elif i == "./" or (i == "../" and res == 0):
                continue
            else:
                res += 1
                
        return res