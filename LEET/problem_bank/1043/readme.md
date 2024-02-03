# 1043. Problem Review

## 1043. Partition Array for Maximum Sum

### Problem Definition
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.


### Approach
- So this problem takes input: arr = [1,15,7,9,2,5,10], k = 3
- We can divide the arr into subarrays of max size k so this would become arr = [[1,15,7],[9],[2,5,10]]
- The ints are changed into the largest value within their subarray so it becomes arr = [[15,15,15],[9],[10,10,10]]
- We add all ints to become 15+15+15+9+10+10+10=84

- To solve this problem we need to first sort the problem. ex: arr = [1,15,7,9,2,5,10] -> arr = [1,2,5,7,9,10,15]
- We then make a subarray of size k composed of the last value and the smallest numbers. arr = [[15,1,2],[10,5,7],[9]]
- For each array, we take max value of that array*len(array)
- Add all of those values to become sum.


- This code doesn't work because I sorted the entire array when it should be continuous instead.

```python
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # To solve this problem we need to first sort the problem. ex: arr = [1,15,7,9,2,5,10] -> arr = [1,2,5,7,9,10,15]
        sorted_arr = sorted(arr)

        # We then make a subarray of size k composed of the last value and the smallest numbers. arr = [[15,1,2],[10,5,7],[9]]
        all_subs = []
        for i in range(len(sorted_arr)//k + (len(sorted_arr) % k > 0)):  # 7//3 + 7%3 = 2 + 1 = 3
            # Append the last value of the array to the sub array
            sub_arr = [sorted_arr.pop()]

            # Append the smallest k-1 values to the sub array
            j = 0
            while j < k-1 and sorted_arr:
                sub_arr.append(sorted_arr.pop(0))
                j += 1

            # Append the sub array to the all_subs array
            all_subs.append(sub_arr)
        # For each array, we take max value of that array*len(array)
        # Add all of those values to become sum.

        return sum([max(sub_arr)*len(sub_arr) for sub_arr in all_subs])
```

### Solution
- The problem is more complicated than I thought.
- We need to check which combination is the largest possible.
- To do this we can use DP.

- n = len(arr)
- dp = [0]*(n+1)
- for i in range(n)
    - cur_max = 0
    - for j in range(1, min(k, i+1), +1):
        - cur_max = max(cur_max, arr[i-j+1])
        - dp[i] = max(dp[i], (dp[i-j] if i >= j else 0) + cur_max * j)
- return dp[n-1]


```python
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Get the length of the array
        n = len(arr)

        # Initialize the dp array
        dp = [0] * (n + 1)

        # Iterate over the array
        for i in range(n):
            # Initialize the max value of the current partition
            cur_max = 0

            # Iterate over all possible sizes of the last subarray
            for j in range(1, min(k, i+1) + 1):
                # Update the max value
                cur_max = max(cur_max, arr[i-j+1])

                # Update dp[i] with the max sum we can get by choosing this size for the last subarray
                dp[i] = max(dp[i], (dp[i-j] if i >= j else 0) + cur_max * j)

        # Return the max sum we can get by partitioning the whole array
        return dp[n-1]
```