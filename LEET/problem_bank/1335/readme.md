# 1335. Problem Review

## 1335. Minimum Difficulty of a Job Schedule

### Problem Definition
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:

    Input: jobDifficulty = [6,5,4,3,2,1], d = 2
    Output: 7
    Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
    Second day you can finish the last job, total difficulty = 1.
    The difficulty of the schedule = 6 + 1 = 7 

Example 2:

    Input: jobDifficulty = [9,9,9], d = 4
    Output: -1
    Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:

    Input: jobDifficulty = [1,1,1], d = 3
    Output: 3
    Explanation: The schedule is one job per day. total difficulty will be 3.
 

Constraints:

    1 <= jobDifficulty.length <= 300
    0 <= jobDifficulty[i] <= 1000
    1 <= d <= 10

### Approach
- Create a condition where if the amount of jobs is smaller than the amount of days, return -1.
- Need to find the minimum possible difficult layout to place the jobs for the respective days.
- Order the priority of how the jobs can be placed: largest to smallest?

### Solution
Since the jobs are dependent, we cannot just sort them by order of difficulty and instead need a dynamic approach. 

- Use dynamic programming to keep track of the minimum difficulty for scheduling a certain number of jobs over a certain number of days.

- For each day, consider the maximum difficulty of the job done on that day and add it to the minimum difficulty calculated for the remaining days and jobs.

```python
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)

        # If we have fewer jobs than days, it's impossible to schedule
        if n < d:
            return -1

        # Initialize DP table with infinities
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]

        # Base case: 0 difficulty for 0 jobs in 0 days
        dp[0][0] = 0

        # Fill the DP table
        for day in range(1, d + 1):
            for i in range(day, n + 1):
                max_diff = 0
                for j in range(i, day - 1, -1):
                    # Max difficulty is compared to decreasing entries
                    max_diff = max(max_diff, jobDifficulty[j - 1])
                    # Max difficulty is added to the min difficulty calculated
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + max_diff)

        return dp[d][n]
