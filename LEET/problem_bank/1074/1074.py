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


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target))  # Output: 4
