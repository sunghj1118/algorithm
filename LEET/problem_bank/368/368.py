from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        lst = []

        # If no numbers in the list, return []
        if len(nums) == 0:
            return []

        # Sort the numbers
        nums.sort()

        # Update solution[i] for each i.
        # Check if nums[i] is divisible by nums[j] and the size of the largest
        # divisible subset ending with nums[j] is larger than the curr size
        # of the largest divible subset ending with nums[i].
        solution = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(solution[i]) < len(solution[j]) + 1:
                    solution[i] = solution[j] + [nums[i]]
        return max(solution, key=len)
