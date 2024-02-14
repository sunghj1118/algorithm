from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
