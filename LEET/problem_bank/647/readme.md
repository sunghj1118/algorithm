# 647. Problem Review

## 647. Palindromic Substrings

### Problem Definition
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



### Approach
- DP

### Solution

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n= len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1

        return count
```