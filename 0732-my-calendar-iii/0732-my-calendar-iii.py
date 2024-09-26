from sortedcontainers import SortedList

class MyCalendarThree:

    def __init__(self):
        self.cal = SortedList()

    def book(self, start: int, end: int) -> int:
        self.cal.add((start, 1))
        self.cal.add((end, -1))
        
        total = 0
        res = 0
        for i, j in self.cal:
            total += j
            res = max(res, total)
            
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)