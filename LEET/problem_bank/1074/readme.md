# 1074. Problem Review

## 1074. Number of Submatrices That Sum to Target

### Problem Definition
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

### Approach
- I need to find the possible combinations of submatrices that are equal to the target.
- Find submatrices.

### Solution
**Approach 1**
- Runs in O(4) time.
- 35 / 40 testcases passed

```python
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def get_submatrices(matrix):
            rows, cols = len(matrix), len(matrix[0])
            for x1 in range(rows):
                for y1 in range(cols):
                    for x2 in range(x1, rows):
                        for y2 in range(y1, cols):
                            yield [[matrix[i][j] for j in range(y1, y2+1)] for i in range(x1, x2+1)]

        def is_sum_equal_target(matrix, target):
            total = sum(sum(row) for row in matrix)
            return total == target

        def get_target_submatrices(matrix, target):
            for submatrix in get_submatrices(matrix):
                if is_sum_equal_target(submatrix, target):
                    yield submatrix

        return len(list(get_target_submatrices(matrix, target)))
```

**Attempt 2**:
- Trying to optimize the find submatrices did decrease the running time but it still isn't enough.
- 39 / 40 testcases passed

```python
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def get_submatrices(matrix):
            rows, cols = len(matrix), len(matrix[0])

            # Compute the 2D prefix sum of the matrix
            prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
            for i in range(rows):
                for j in range(cols):
                    prefix_sum[i+1][j+1] = matrix[i][j] + prefix_sum[i +
                                                                     1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]

            # Generate all submatrices
            for x1 in range(rows):
                for y1 in range(cols):
                    for x2 in range(x1, rows):
                        for y2 in range(y1, cols):
                            total = prefix_sum[x2+1][y2+1] - prefix_sum[x2 +
                                                                        1][y1] - prefix_sum[x1][y2+1] + prefix_sum[x1][y1]
                            yield total

        def get_target_submatrices(matrix, target):
            for sum_submatrix in get_submatrices(matrix):
                if sum_submatrix == target:
                    yield sum_submatrix

        return len(list(get_target_submatrices(matrix, target)))


matrix = [[1, -1], [-1, 1]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target))
```


**Solution**
- Using a 2D prefix sum decreases the running time greatly.

```python
from typing import List
from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Compute the 2D prefix sum of the matrix
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i -
                                                                 1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

        count = 0
        # Iterate over all pairs of rows
        for r1 in range(1, rows + 1):
            for r2 in range(r1):
                counter = Counter({0: 1})
                cur = 0
                # Use a hash map to find the sum of submatrices
                for c in range(1, cols + 1):
                    cur = prefix_sum[r1][c] - prefix_sum[r2][c]
                    count += counter[cur - target]
                    counter[cur] += 1

        return count
```