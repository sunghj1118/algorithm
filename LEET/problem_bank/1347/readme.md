# 1347. Problem Review

## 1347. Minimum Number of Steps to Make Two Strings Anagram

### Problem Definition
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

### Approach
- Find how many letters are different from each other.
- Create dictionaries for string s and t.
- For # chars in s, if the # chars in t is different, add diff to counter.
- How to replace chars that are in excess with chars that are needed?


### Solution
- Create dictionary with counts for chars.
- Subtract the amount of chars in second dict from the first dict.
- If there are more positive values in the first dict then the the output is the sum of counts in dict.
- However, if there are more negative counts, then the output is that value.

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_s = {}
        dict_t = {}

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1

        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        for char in dict_s:
            if char in dict_t:
                dict_s[char] -= dict_t[char]

        pos_count = sum(v for v in dict_s.values() if v > 0)
        neg_count = sum(v for v in dict_s.values() if v < 0)

        if pos_count >= neg_count:
            return pos_count
        else:
            return abs(neg_count)
