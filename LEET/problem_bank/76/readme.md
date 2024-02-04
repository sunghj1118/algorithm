# 76. Problem Review

## 76. Minimum Window Substring

### Problem Definition
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

### Approach

**First Impression**:
- We could go adding one letter at a time to the right one by one.
    - We create a dictionary of the second string and before adding a new letter, we check if all letters from t are in s.
- How do we check if it is the shortest possible string?


**Attempt**:
- Sliding window

- 1)Create a dict_t for string t
- 2)Create a counter to check whether the window matches the target string t.
    - When the char from s is in dict_t, decrease the count in dict_t. When the count is 0, increase the counter. When the counter equals the size of dict_t, you know the substring s contains t.
- 3)Try to minimize the window
    - Move the left pointer of the window.
    - If the char at the left pointer exists in dict_t, increase the count in dict_t.
    - When the count is greater than 0, decrease the counter. Repeat step 3 until the counter is no longer valid.
- 4)Repeat step 2.


### Solution
- Do a sliding window
- Check if the chars in string t were fulfilled.
    - If true, try to shorten the string until the condition is broken.
- Move to the right until condition is satisfied again.

```python
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If either string is empty, return empty string
        if not t or not s:
            return ""

        # Create dictionary that has counts of char occurences of string t
        dict_t = Counter(t)

        # The number of unique characters in t
        required = len(dict_t)

        # Two pointers, left and right
        l, r = 0, 0

        # The number of unique chars in the current window that match the chars in t
        formed = 0

        # A dict to keep track of all the unique chars in the current window
        window_counts = {}

        # The length of the smallest window, and the left and right indices of that window
        ans = float("inf"), None, None

        # While the entire string hasn't been searched
        while r < len(s):
            # Add the char from s to the window_counts dictionary
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If this character is needed and its count is enough, increment increment the formed count
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window until the point where it ceases to be desirable
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)

                # The character at the position pointed by the 'l' pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window
                l += 1

            # Keep expanding the window once we are done contracting
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```