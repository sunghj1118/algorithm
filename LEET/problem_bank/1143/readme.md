# 1143. Problem Review

## 1143. Longest Common Subsequence

### Problem Definition
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

### Approach
- Create a 2D array dp. dp[i][j] represents the length of the longest common subseq (LCS) of text1[0...i] and text2[0...j]
- Initialize dp[i][0] and dp[0][j] to 0 for all i and j, because the LCS of any string with an empty string is an empty string.
- For each char in text1 and text2, if text1[i] == text2[j], then the length of the LCS would be dp[i-1][j-1] + 1. Otherwise the length of the LCS would be the maximum of dp[i-1][j] and dp[i][j-1].
- The length of the LCS of text1 and text2 would be dp[m][n], where m and n are the lengths of text1 and text2.


### Solution
Create an array of size of n*n where n is the length of the shorter string and go comparing the letters between the first and second and find the max between the previous pos in i and pos in j.

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
