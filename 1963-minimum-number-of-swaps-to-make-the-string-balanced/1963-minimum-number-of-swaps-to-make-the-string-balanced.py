class Solution(object):
    def minSwaps(self, s):
        res = 0
        val = 0
        
        for i in s:
            if i == "[":
                val += 1
            elif i == "]":
                val -= 1
            res = min(res, val)
            
        return (-res + 1) // 2