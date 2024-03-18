import random
class RandomizedSet:
    
    def __init__(self):
        self.lis = []

    def insert(self, val: int) -> bool:
        if val not in self.lis:
            self.lis.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if self.lis and val in self.lis:
            self.lis.remove(val)
            return True
        else:
            return False
            

    def getRandom(self) -> int:
        return random.choice(self.lis)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()