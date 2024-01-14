# 1657. Problem Review

## 1657. Determine if Two Strings Are Close

### Problem Definition
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

### Approach
- Create two dictionaries with the amount of counts for each string.

### Attempt#1
Didn't work because it doesn't consider if Operation 2 works by replacing ALL occurences of some character.
<br> 132/153 passed

```python
# Subtract char counts in dict1 from dict2
        for c in dict1:
            if c in dict2:
                dict1[c] -= dict2[c]

        x = sum(n for n in dict1.values())
        if x == 0:
            return True
        else:
            return False
```

### Attempt#2
146 / 153 testcases passed
<br> 
word1 = "zzazicgvzwntnneauziwfzlrzkynzschzdkbmpqbolwgvxjava" <br>
word2 = "uequrwuzhaudmnuqjuolkeszcyfqzqizrdrxpuvuygytbucwog"

expected: true

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        dict1 = {}
        dict2 = {}

        # Create two dictionaries with char counts for each word
        for c in word1:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1

        for c in word2:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1

        # Check if char types are the same
        if len(dict1) != len(dict2):
            return False

        # Check presence
        for c in dict1:
            if c not in dict2:
                return False

        temp_d1 = dict1.copy()
        temp_d2 = dict2.copy()

        # If char counts in dict1 and dict2 are equal, delete them
        for c in temp_d1:
            if (c in temp_d2) and (temp_d1[c] == temp_d2[c]):
                del dict1[c]
                del dict2[c]

        sorted_dict1 = {k:v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
        sorted_dict2 = {k:v for k, v in sorted(dict2.items(), key=lambda item: item[1])}

        # Check if the expected char count is in one of the char counts in the same dict
        for c in dict1:
            for d in dict1:
                if (c in dict2) and (dict1[c] == dict2[c]):
                    continue

                if (c in dict2) and dict2[c] == dict1[d]:
                    dict1[c], dict1[d] = dict1[d], dict1[c]

        for c in dict1:
            if (c in temp_d2) and (dict1[c] != dict2[c]):
                return False

        return True
```


### Solution
- Frequency Counting
- Checking Presence of Characters
- Sorting Frequencies
- Comparing Sorted Frequencies
- Final Result

Wow this works within 3 lines. The key idea behind this problem was that we need to sort by the frequencies and the frequencies should correspond to each other.

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return (c1.keys() == c2.keys()) and (sorted(c1.values()) == sorted(c2.values()))
