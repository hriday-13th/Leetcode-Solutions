class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = abs(ax2 - ax1) * abs(ay2 - ay1)
        b = abs(bx2 - bx1) * abs(by2 - by1)
        
        if ax1 >= bx2 or bx1 >= ax2 or ay1 >= by2 or by1 >= ay2:
            return a + b
        
        x = [ax1, ax2, bx1, bx2]
        y = [ay1, ay2, by1, by2]
        
        x.sort()
        y.sort()
        
        a1, a2 = x[1], x[2]
        b1, b2 = y[1], y[2]
        
        l1, l2 = abs(a2 - a1), abs(b2 - b1)
        
        return a + b - l1 * l2