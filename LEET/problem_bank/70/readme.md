# 70. Problem Review

## 70. Climbing Stairs

### Problem Definition
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Approach
- There are only two base cases: 1 or 2. The rest are a sum of the previous cases.

### Solution
Provide a detailed explanation of your solution. Include code snippets if possible.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
