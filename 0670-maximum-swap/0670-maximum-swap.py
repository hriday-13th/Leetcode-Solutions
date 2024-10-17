class Solution(object):
    def maximumSwap(self, num):
        num = list(str(num))
        
        max_digit = "0"
        si, sj = -1, -1
        max_i = -1
        
        for i in reversed(range(len(num))):
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i
            if num[i] < max_digit:
                si, sj = i, max_i
                
        num[si], num[sj] = num[sj], num[si]
        
        return int(''.join(num))