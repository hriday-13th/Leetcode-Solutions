class StockSpanner:

    def __init__(self):
        self.stack = deque()
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
            
        if self.stack:
            span = self.day - self.stack[-1][1]
        else:
            span = self.day
            
        self.stack.append((price,self.day))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)