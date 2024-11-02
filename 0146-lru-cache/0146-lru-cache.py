class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}
        
    def addNode(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        
    def deleteNode(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            self.deleteNode(node)
            self.addNode(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.deleteNode(curr)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        self.addNode(Node(key, value))
        self.m[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)