from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict = Counter(nums)
        dup = -1
        missing = -1

        for i in range(1, len(nums)+1):
            if i not in dict:
                missing = i
            elif dict[i] == 2:
                dup = i

        return [dup, missing]
