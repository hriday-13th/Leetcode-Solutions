class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = []
        self.len = 0
        self.max_len = k

    def insertFront(self, value: int) -> bool:
        if self.len < self.max_len:
            self.arr.insert(0, value)
            self.len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.len < self.max_len:
            self.arr.append(value)
            self.len += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.len > 0:
            self.arr.pop(0)
            self.len -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.len > 0:
            self.arr.pop()
            self.len -= 1
            return True
        return False


    def getFront(self) -> int:
        if self.len > 0:
            return self.arr[0]
        return -1


    def getRear(self) -> int:
        if self.len > 0:
            return self.arr[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.max_len


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()