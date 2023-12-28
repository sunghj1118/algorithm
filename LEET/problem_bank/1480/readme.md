# 1480. Problem Review

## 1480. Running Sum of 1d Array

### Problem Definition
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]
 

Constraints:

    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6

### Approach
- Need to add the next value in the list to the overall sum as it goes checking every single value in the list.
- To do this, it should initialize another variable running_sum that keeps track of the overall sum.

### Solution
- Initialize running_sum var.
- Initialize result list to append the results.
- For loop for number in nums list provided.
- Add number in list to running_sum var and then append that value to the result list.

```python
class Solution(object):
    def runningSum(self, nums):
        running_sum = 0
        result = []

        for num in nums:
            running_sum += num
            result.append(running_sum)

        return result

