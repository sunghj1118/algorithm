# 629. Problem Review

## 629. K Inverse Pairs Array

### Problem Definition
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo `10^9 + 7`.

### Approach
오. 뭔가 알 것 같으면서도 잘 모르겠다. 음. 그니까 다음에 오는 숫자가 지금 숫자보다 작아야 된다는 말인데, 이런 짝이 가능한 경우의 수가 몇개가 있는지 출력해야 한다.

그면 일단 n이 주어지니까 3이면 0,1,2 하고나서 3으로 할 수 있는 모든 경우의 수에 대하여 inv_pair가 몇개가 가능한지 확인을 해야 하고, 그 값이 우리가 원하는 k와 같을 경우에, counter를 1올리면 된다.

### Solution

**APPROACH 1**
- 이렇게 하니까 예제는 풀 수 있는데, 답은 틀린다. 
11 / 80 testcases passed <br>
Time Limit Exceeded

어떻게 하면 더 빠르게 만들 수 있을까? 일단 permutation을 다 만들기 때문에 지금은 O(n!) 시간복잡도를 갖고 있어서 느리다.
DP를 사용해보자.


```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        def generate_permutations(nums):
            if len(nums) <= 1:
                return [nums]
            else:
                permutations = []
                for i in range(len(nums)):
                    rest = nums[:i] + nums[i+1:]
                    for p in generate_permutations(rest):
                        permutations.append([nums[i]] + p)
                return permutations

        def count_inverse_pairs(nums):
            count = 0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] > nums[j]:
                        count += 1
            return count

        count = 0
        nums = list(range(1, n+1))
        perms = generate_permutations(nums)
        for p in perms:
            if count_inverse_pairs(p) == k:
                count = (count + 1) % MOD
        return count
```


**APPROACH 2**
- DP
- Create 2D DP array.
    - dp[i][j] represents nums of permutations of size i that have exactly j inverse pairs.

```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7 # MOD를 선언, 10^9 + 7로 초기화

        # DP 테이블을 만들고, 0으로 초기화
        dp = [[0] * (k+1) for _ in range(n+1)]

        # 0개의 역순쌍을 가지고 있는 크기 0과 크기 1의 수열은 1개이다.
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1

            # 1부터 k까지의 역순쌍을 가지고 있는 수열의 개수를 구한다.
            for j in range(1, k+1):
                # j개의 역순쌍을 가지고 있는 크기 i의 수열의 개수는 다음의 합과 같다:
                # - j개의 역순쌍을 가지고 있는 크기 i-1의 수열의 개수
                # - j-1개의 역순쌍을 가지고 있는 크기 i-1의 수열의 개수
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

                # j-i가 0보다 크거나 같은 경우, j개의 역순쌍을 가지고 있는 크기 i의 수열의 개수는 다음의 합과 같다:
                # - j-i개의 역순쌍을 가지고 있는 크기 i의 수열의 개수
                if j-i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i] + MOD) % MOD
        
        # n개의 원소를 가지고 있는 수열의 개수를 반환한다.
        return dp[n][k]
```

