# 380. Problem Review

## 380. Insert Delete GetRandom O(1)

### Problem Definition
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

### Approach
- Just create a set.
- If else statements whether the values in sets or not.
- Import random module.

### Solution
After changing the random to a list instead of a dictionary, the program increased from beating 10% to beating 80%.

Original:
```python
import random


class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.sample(list(self.set), 1)[0]
```

Improved:

```python
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

```