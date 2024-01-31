# 739. Problem Review

## 739. Daily Temperatures

### Problem Definition
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

### Approach
- We could cycle through the entire list for every single entry, comparing and increasing the count for that day by 1 if it is smaller or equal to the entry.

### Solution
### Attempt#1
- 35 / 48 testcases passed
- Time Limit Exceeded, currently O(n^2)

```python
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = []

        for current in range(len(temperatures)):
            temp = 0
            for days in range(current + 1, len(temperatures)):
                if temperatures[current] >= temperatures[days]:
                    temp += 1

                if temperatures[current] < temperatures[days]:
                    temp += 1
                    wait_days.append(temp)
                    break
                elif days == (len(temperatures)-1):
                    temp = 0
                    wait_days.append(temp)
                    break

        wait_days.append(0)
        return wait_days
```

### Attempt#2
- Use a stack to keep track of unresolved temps.

```python
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last_day = stack.pop()
                answer[last_day] = i - last_day
            stack.append(i)
        return answer
```
