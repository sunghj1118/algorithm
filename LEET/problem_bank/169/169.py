from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        majority = 0
        for value in dictionary:
            if dictionary[value] > (len(nums) / 2):
                majority = value

        return majority


print(Solution().majorityElement([3, 2, 3]))
