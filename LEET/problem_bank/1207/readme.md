# 1207. Problem Review

## 1207. Unique Number of Occurrences

### Problem Definition
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


### Approach
- Create a dictionary and check if any values overlap

### Solution
- If values in set, return false, else add it to set.

```python
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for v in c.values():
            if v in s:
                return False
            s.add(v)
        return True
