from random import choice


class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.list.remove(val)
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()

print(param_1)
print(param_2)
print(param_3)
