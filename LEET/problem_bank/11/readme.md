# 11. Problem Review

## 11. Container With Most Water

### Problem Definition
We need to find the container that can store the most water given a list of heights. 

### Approach
I will go through each of the heights and calculate the area of the container that can be formed with the current height and the height at the other end of the list. I will keep track of the maximum area found so far and return it at the end.

### Solution
- We go counting one by one starting from the leftmost height.
- For each height, we calculate the area with the rightmost height.
- We keep track of the maximum area found so far.
- We return the maximum area found.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```