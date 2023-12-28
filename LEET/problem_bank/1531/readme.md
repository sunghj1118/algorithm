# 1531. Problem Review

## 1531. String Compression II

### Problem Definition
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

    Input: s = "aaabcccd", k = 2
    Output: 4
    Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

Example 2:

    Input: s = "aabbaa", k = 2
    Output: 2
    Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.

Example 3:

    Input: s = "aaaaaaaaaaa", k = 0
    Output: 3
    Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
 

Constraints:

    1 <= s.length <= 100
    0 <= k <= s.length
    s contains only lowercase English letters.

### Approach
Step 1:
- We first need to check the different ways we can shorten the string given k deletable characters.
- After testing though possible deletable options, we need to check if the length of the string is smaller than our smallest length up to now.
- Output is our smallest string length after cycling through all possible removable strings.
- In order to find out which characters to delete, we could try to create a key-value pair dictionary that shows the amount of characters for each character in the string.

Step 2:
- Then, we need to cycle through the dictionary to see how to shorten the string as much as possible. The best way to shorten the string is to delete a single character if there is only one such character. The next best way would be to delete two characters of the same type, thus removing two characters from the final string: the character and the amount of such characters. In other words, the best way is to remove the character entirely if possible.
- It is better to remove a character with 2 entries rather than a single character entry.

### Attempts

Attempt #1: In this first attempt I tried the following.
- Create a dictionary with the amount of chracters.
- Sort the characters based on deletion priority.
- Delete characters while k > 0.
- Count the string length.

However, this didn't work because it doesn't account for consecutivity which causes it to fail the following test case.

    Input
    s = "bababbaba"
    k = 1

    Output: 4
    Expected: 7

Shortened down, this would become babab2aba. By deleting an 'a' before or after b2, we can delete the 'a' itself, and combine the previous or consequent b into b3. This shortens the string from length 9 to up to 7.

```python
from collections import defaultdict


class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def run_length_encode_length(char_sequences):
            length = 0
            for char, count in char_sequences.items():
                if count == 1:
                    # Just the character, no count
                    length += 1
                else:
                    # Character plus the length of the count in digits
                    length += 1 + len(str(count))
            return length

        # Count sequences of each character
        char_sequences = defaultdict(int)
        for char in s:
            char_sequences[char] += 1

        # Sort based on deletion priority
        def deletion_priority(char):
            count = char_sequences[char]
            if count <= k:
                # First priority: characters that can be completely deleted
                return (1, count)
            if count == 2:
                # Second priority: characters that can be reduced from 2 to 1
                return (2, count)
            if 10 <= count <= 100 and count - k < 10:
                # Third priority: reducing from two digits to one
                return (3, -count)
            return (4, -count)   # Other characters

        sorted_chars = sorted(char_sequences, key=deletion_priority)

        # Delete characters strategically
        for char in sorted_chars:
            if k == 0:
                break
            if char_sequences[char] <= k:
                k -= char_sequences[char]
                del char_sequences[char]
            else:
                char_sequences[char] -= k
                k = 0

        # Calculate the length of the encoded string after deletions
        return run_length_encode_length(char_sequences)
```

### Solution
I was able to solve this on the second attempt after I refactored it entirely into dynamic programming by creating a dp table. The table would check every step possible after making j deletions.

The algorithm then either (a) doesn't delete the character (b) deletes the character and finally (c) aggregates consecutive characters to check whether the impact of deletions were positive.

Finally, when the string length is equal to the original length, the ideal compressed length is stored in k.

```python
class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        def encode_length(count):
            if count == 0:
                return 0
            elif count == 1:
                return 1
            elif count < 10:
                return 2
            elif count < 100:
                return 3
            else:
                return 4

        for i in range(1, n + 1):
            for j in range(k + 1):
                # Delete the current character
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

                # Keep the current character
                count, deletions = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        count += 1
                    else:
                        deletions += 1
                        if deletions > j:
                            break
                    dp[i][j] = min(dp[i][j], dp[l - 1]
                                   [j - deletions] + encode_length(count))

        return dp[n][k]
