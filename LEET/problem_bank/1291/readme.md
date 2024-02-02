# 1291. Problem Review

## 1291. Sequential Digits

### Problem Definition
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

### Approach
- For i in range(low, high)
    - if integer has sequential digits
        - append to list

- This returns timeout error because it iterates over every number in the range from low and high.
- A more efficient approach would be to generate only the sequential numbers in the range.

```python
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output = []

        for i in range(low, high + 1):
            # Convert integer to string
            s = str(i)

            # Check if integer is sequential
            if all(int(s[j]) - int(s[j-1]) == 1 for j in range(1, len(s))):
                output.append(i)

        return output
```

### Solution
- Generate sequential integers of lengths between the high and low inputs.

```python
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Initialize an empty list to store the output
        output = []

        # Loop over the lengths of the numbers from low to high
        for length in range(len(str(low)), len(str(high)) + 1):

            # Iterate over the possible starting digits
            for start in range(1, 10):
                # Generate a sequential number of the current length starting with the current digit
                num = int(''.join(str(start + i) for i in range(length)))
                if start + length > 10:  # if the number contains a digit greater than 9, break the loop
                    break

                # If the number is within the range, append it to the output list
                if low <= num <= high:
                    output.append(num)
        # Sort the output list and return it
        return sorted(output)
```