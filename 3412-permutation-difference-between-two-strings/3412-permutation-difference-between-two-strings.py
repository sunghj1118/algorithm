class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(t.index(ch) - s.index(ch)) for ch in s)