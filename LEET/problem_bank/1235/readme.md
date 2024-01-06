# 1235. Problem Review

## 1235. Maximum Profit in Job Scheduling

### Problem Definition
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

### Approach
- This is very obviously DP.
- How could we break this problem?
- We could have a list of tuples representing the jobs.
- We need to find the max possible net profit of every job with regards to their previous jobs.
- Return max value from the array of job profits.

### Attempt 1: 
### Checking every job against every other job to see if they overlap, results in a time complexity of O(n^2)
This attempt failed at the following test case:

    startTime = [6,15,7,11,1,3,16,2]
    endTime = [19,18,19,16,10,8,19,8]
    profit = [2,9,1,19,5,7,3,19]

    Output: 22 vs Expected: 41

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Using zip to combine the three lists into tuples
        job_schedule = list(zip(startTime, endTime, profit))

        # For each job, initialize an empty list to store the max profit for each job
        max_profits = [0] * len(job_schedule)

        # For each job, find the max profit
        for i in range(len(job_schedule)):
            # Initialize the max profit for the current job
            max_profit = 0
            # For each job, check if the current job can be done
            for j in range(i):
                # If the current job can be done, then update the max profit
                if job_schedule[j][1] <= job_schedule[i][0]:
                    max_profit = max(max_profit, max_profits[j])
            # Update the max profit for the current job
            max_profits[i] = max_profit + job_schedule[i][2]

        # Now job_schedule is a list of tuples, where each tuple is (startTime, endTime, profit)
        return max(max_profits)
```

### Attempt 2: Add sort
Added sort but this caused Time Limit Exceeded in one testcase. Passed more cases than before.
<br> 23 / 31 testcases passed.
<br> The testcase 23 is incredibly long (300< lines), which is unsolvable with the current slow implementation. I need to decrease the time complexity.

```python
# Sort the job schedule by the end time
job_schedule.sort(key=lambda x: x[1])
```

### Attempt 2: DP + Binary Search
25 / 31 testcases passed
<br> Still failing really large cases.

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Using zip to combine the three lists into tuples
        jobs = list(zip(startTime, endTime, profit))

        # For each job, initialize an empty list to store the max profit for each job
        dp = [0] * (len(jobs) + 1)

        # Sort the job schedule by the end time
        jobs.sort(key=lambda x: x[1])

        # Start the DP calculation with binary search
        for i in range(1, len(jobs) + 1):
            # Binary Search for the latest job that ends before the current job starts
            index = bisect_right([jobs[j][1]
                                 for j in range(i)], jobs[i - 1][0]) - 1

            # Calculate the max profit for the current job
            dp[i] = max(dp[i - 1], jobs[i - 1][2] + dp[index + 1])

        return dp[-1]
```



### Solution
Couldn't solve it by myself so had to look up the answers. 

```python
from typing import List
import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)
        
        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            current_start, _, current_profit = jobs[i]
            # Find the latest job that finishes before the current job starts
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]
                
            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]


