class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.highest_timestamp = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.highest_timestamp = max(self.highest_timestamp, timestamp)
        
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.highest_timestamp]

    def maximum(self) -> int:
        p, t = heapq.heappop(self.max_heap)
        
        while -p != self.timestamps[t]:
            p, t = heapq.heappop(self.max_heap)
            
        heapq.heappush(self.max_heap, (p, t))
        
        return -p

    def minimum(self) -> int:
        p, t = heapq.heappop(self.min_heap)
        
        while p != self.timestamps[t]:
            p, t = heapq.heappop(self.min_heap)
            
        heapq.heappush(self.min_heap, (p, t))
        
        return p


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()