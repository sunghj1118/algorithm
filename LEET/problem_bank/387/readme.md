# 387. Problem Review

## 387. First Unique Character in a String

### Problem Definition
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

### Approach
- Go through each letter in the string. 
- If the letter's freq is equal to 1, return the current letter's index.
- If we cycle through the entire string and there's no return, then return -1.

### Solution

```python
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = Counter(s)
        count = 0

        for index, letter in enumerate(s):
            if dict_s[letter] == 1:
                return index

        return -1


s = "leetcode"
print(Solution().firstUniqChar(s))
```