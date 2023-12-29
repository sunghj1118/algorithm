# 1578. Problem Review

## 1578. Minimum Time to Make Rope Colorful

### Problem Definition
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

### Approach
- Need to cycle through the string and compare the first and second value.
- See if they are the same character, if so, remove the one with the smaller neededTime.

### Attempt #1
Doesn't work at colors = "aaabbbabbbb", neededTime = [3,5,10,7,5,3,5,5,4,8,1].
This is because if there are several consecutive repeated colors, it only compares two at a time so if there are three or more consecutive characters, it doesn't account for those. For example, aaaa will result in a(aa)a when it needs to delete all 'a' chars but one.

```python
class Solution(object):
    def minCost(self, colors, neededTime):
        cost = 0

        for i in range(len(colors) - 1):
            if colors[i] == colors[i + 1]:
                if neededTime[i] >= neededTime[i+1]:
                    cost += neededTime[i+1]
                else:
                    cost += neededTime[i]

        return cost
```

### Solution
- Instead of using a for loop, we replaced it with a while loop to iterate over the string for the entire consecutive and equivalent characters. Out of these characters, it will only keep the maxCost, removing all others.


```python
class Solution(object):
    def minCost(self, colors, neededTime):
        cost = 0
        i = 0

        while i < len(colors) -1:
            if colors[i] == colors[i+1]:
                total_time = neededTime[i]
                max_time = neededTime[i]

                # Move through sequence of identical chars
                while i < len(colors)-1 and colors[i] == colors[i+1]:
                    total_time += neededTime[i+1]
                    max_time = max(max_time, neededTime[i+1])
                    i += 1
                
                cost += total_time - max_time
            else:
                i += 1
        
        return cost
