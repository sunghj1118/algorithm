# 1704. Problem Review

## 1704. Determine if String Halves Are Alike

### Problem Definition
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

### Approach
- Split string by slicing. From beginning to len(s)/2 and len(s)/2 to end
- Get sum of all vowels in first half and second half
- Compare and return true if equal

### Solution
- Same as approach

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first, second = s[:len(s)//2], s[len(s)//2:]
        return sum([1 for c in first if c in 'aeiouAEIOU']) == sum([1 for c in second if c in 'aeiouAEIOU'])

