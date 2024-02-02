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


# Example 1
nums = [15, 13, 12, 13, 12, 14, 12, 2, 3, 13,
        12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2]
k = 2

# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
print(Solution().divideArray(nums, k))
