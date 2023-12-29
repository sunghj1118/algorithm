# 412. Problem Review

## 412. Fizz Buzz


### Problem Definition
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5. <br>
answer[i] == "Fizz" if i is divisible by 3.<br>
answer[i] == "Buzz" if i is divisible by 5.<br>
answer[i] == i (as a string) if none of the above conditions are true.

### Approach
- Do a for loop that appends a string number depending on the value i.

### Solution
- Do for loop from 1 to n+1.
- if-elif-else for conditions provided.
- return list

```python
class Solution(object):
    def fizzBuzz(self, n):
        str_arr = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                str_arr.append("FizzBuzz")
            elif i % 3 == 0:
                str_arr.append("Fizz")
            elif i % 5 == 0:
                str_arr.append("Buzz")
            else:
                str_arr.append(str(i))

        return str_arr
