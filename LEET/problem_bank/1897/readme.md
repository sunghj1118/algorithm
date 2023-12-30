# 1897. Problem Review

## 1897. Redistribute Characters to Make All Strings Equal

### Problem Definition

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

### Approach
- Create a dictionary for each word selected.
- Compare the two dictionaries.
- If they are equal, then they should be able to be the same.
- Q: Can words be deleted entirely by moving their letters into other words?

### Solution
- Create dictionary for the count of chars for all words in the List.
- Check if the count of each char in the dictionary is divisible by the amount of words.

```python
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        char_count = {}

        # Count the number of times each character appears in the list of words
        for word in words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        # If the number of times a character appears is not divisible by the number of words, return False
        for char in char_count:
            if char_count[char] % len(words) != 0:
                return False

        return True
