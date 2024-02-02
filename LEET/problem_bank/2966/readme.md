# 2966. Problem Review

## 2966. Divide Array Into Arrays With Max Difference

### Problem Definition
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

### Approach
- Sort the array
- Possible = True
- Divide the array into arrays of size three
    - For numbers in array:
        - If the difference between next number in the array and the current one is larger than k, possible = False.

- 984 / 1115 testcases passed
- This test fails because the difference between the last int in a subarray and the first int in the next subarray is larger than k, when this doesn't matter.
    - We need to divide the array into subarrays first and then compare for each subarray.

```python
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # If the length of the array is not a multiple of 3, return an empty array
        if len(nums) % 3 != 0:
            return []

        # Sort the array
        nums.sort()

        # Possible = True
        possible = True

        # Divide the array into arrays of size three
        # For numbers in array:
        for i in range(len(nums) - 1):
            # If the difference between next number in the array and the current one is larger than k, possible = False
            if nums[i + 1] - nums[i] > k:
                possible = False
                break

        if not possible:
            return []  # Return empty array
        else:
            # Return the array divided into arrays of size three
            return [nums[i:i + 3] for i in range(0, len(nums), 3)]
```


**Attempt 2**

- 1109 / 1115 testcases passed
- Don't understand why this isn't working for testcase:
    - nums = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]
    - k = 2
    - Shouln't the following output work?
    - [[2,2,2],[2,3,5],[12,12,12],[12,12,12],[13,13,13],[13,13,14],[14,14,15]]

```python
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # If the length of the array is not a multiple of 3, return an empty array
        if len(nums) % 3 != 0:
            return []

        # Sort the array
        nums.sort()

        # Possible = True
        possible = True

        # Divide the array into arrays of size three
        arrays3 = [nums[i:i + 3] for i in range(0, len(nums), 3)]

        # For each array of size three:
        for arrays in arrays3:
            # For numbers in array:
            for i in range(len(arrays) - 1):
                # If the difference between next number in the array and the current one is larger than k, possible = False
                if arrays[i + 1] - arrays[i] > k:
                    possible = False
                    break

        if not possible:
            return []  # Return empty array
        else:
            # Return the array divided into arrays of size three
            return arrays3
```

### Solution
- This is the answer but I don't understand why.

```python
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans
```
