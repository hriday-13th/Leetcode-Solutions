from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.cal = SortedList()

    def book(self, start: int, end: int) -> bool:
        self.cal.add((start, 1))
        self.cal.add((end, -1))
        
        total = 0
        for i, j in self.cal:
            total += j
            if total == 3:
                self.cal.remove((start, 1))
                self.cal.remove((end, -1))
                return False
            
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)