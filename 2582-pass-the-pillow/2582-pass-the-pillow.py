class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        l = n - 1
        time = time % (2 * l)
        
        if time > l:
            return 2*l - time + 1
        else:
            return time + 1