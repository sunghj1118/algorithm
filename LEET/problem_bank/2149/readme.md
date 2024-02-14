# 2149. Problem Review

## 2149. Rearrange Array Elements by Sign

### Problem Definition
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.




### Approach
- make pos and neg list
- for i in range(len(pos)):
    - append pos
    - append neg
- return result

### Solution


```python
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
```