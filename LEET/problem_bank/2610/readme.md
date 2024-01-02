# 2610. Problem Review

## 2610. Convert an Array Into a 2D Array With Conditions

### Problem Definition
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.


### Approach
- Create a dictionary with the frequencies of each character.

### Solution
- Create a dictionary with the frequencies of each character.
- For every char in the dictionary, append them to a temporary list.
- Subtract one value from the dictionary every time I do this.
- If the char is 0, then remove it entirely from the dictionary.

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqdict = {}
        for num in nums:
            if num in freqdict:
                freqdict[num] += 1
            else:
                freqdict[num] = 1

        result = []
        while freqdict:
            row = []
            # Iterate over the items in the dictionary
            for num in list(freqdict.keys()):
                row.append(num)
                freqdict[num] -= 1
                # Remove the item from the dictionary if the count is 0
                if freqdict[num] == 0:
                    del freqdict[num]
            result.append(row)

        return result

