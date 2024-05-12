# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 0, n
        
        while True:
            m = (l+h) // 2
            val = guess(m)
            if val == 0:
                return m
            elif val == -1:
                h = m - 1
            else:
                l = m + 1