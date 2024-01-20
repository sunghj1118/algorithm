# 907. Problem Review

## 907. Sum of Subarray Minimums

### Problem Definition
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.

### Approach
- Find subarrays.
- Find min values.
- Sum.

### Attempt 1
68 / 87 testcases passed

Memory limit exceeded. <br>
Creating subarrays and storing them in memory causes a memory issue. Adding the min value to the sum right away is much better.

```python
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        subarrays = []
        # generate all subarrays
        for i in range(n):
            for j in range(i, n):
                subarrays.append(arr[i:j+1])

        # add min values of all subarrays
        total = 0
        for subarray in subarrays:
            total += min(subarray)

        return total
```

### Approach 2
73 / 87 testcases passed.

Adding sums right away was better but still returning wrong answer at some point. <br>
Researching for why this happened led to finding out that this is probably due to integer overflow. <br>
The problem requires us to return the modulo 10^9 + 7 to avoid overflow, instead of promoting it into a long.

I tried several ways of performing the modulo calculation but most failed except the last one.

Fail#1: <br>
total += min(arr[i:j+1]) % (10**9 + 7)

Fail#2: <br>
total = (total + min(arr[i:j+1])) % (10**9 + 7)

### Approach 3
75 / 87 testcases passed

Time limit exceeded. <br>
Currently, this creates all subarrays and calculates the min for each which is an O(n^3). <br>
We need a more efficient approach. <br>


### Solution

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s = []
        total = 0
        mod = 10**9 + 7
        for i, x in enumerate(arr):
            while s and arr[s[-1]] > x:
                j = s.pop()
                k = s[-1] if s else -1
                total = (total + arr[j] * (i - j)*(j - k)) % mod
            s.append(i)

        while s:
            j = s.pop()
            k = s[-1] if s else -1
            total = (total + arr[j] * (len(arr) - j) * (j - k)) % mod

        return total
