from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for v in c.values():
            if v in s:
                return False
            s.add(v)
        return True


solution = Solution()
print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
