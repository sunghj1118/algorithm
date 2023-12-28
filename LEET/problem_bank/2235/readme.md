# Problem Review

## 2235. Add Two Integers

### Problem Definition
Given two integers num1 and num2, return the sum of the two integers.

**Example 1:**

    Input: num1 = 12, num2 = 5
    Output: 17
    Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

**Example 2:**

    Input: num1 = -10, num2 = 4
    Output: -6
    Explanation: num1 + num2 = -6, so -6 is returned.
 

**Constraints:**

    -100 <= num1, num2 <= 100


### Approach
- Need to return the sum of the two numbers.
- Require checking the constraints.
- Implement exception in the case input doesn't pass constraints.

### Solution
- Create a if-else statement to check constraints.
- If it passes, return the sum.
- Else, return nothing.

```python
class Solution(object):
    def sum(self, num1, num2):
        if (-100 <= num1 and num2 <= 100):
            return num1 + num2
        else:
            return
