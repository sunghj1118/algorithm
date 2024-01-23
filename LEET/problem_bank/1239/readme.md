# 1239. Problem Review

## 1239. Maximum Length of a Concatenated String with Unique Characters

### Problem Definition
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

### Approach
- We need to check if the characters overlap for any two subsequences.
    - If they don't, they can be concatenated to be a longer subsequence.
    - Store the length of the subsequence as max.
        - If the new subsequence is longer than the set max, replace it.
- How could we check for each subsequence combination?
    - DP and store the largest possible sequence at that point? What if the combination of the first and second is shorter than the combination of the first and third?
    - DFS: Add each string if the string doesn't overlap.

### Solution
Provide a detailed explanation of your solution. Include code snippets if possible.

```python
# Code snippet here
