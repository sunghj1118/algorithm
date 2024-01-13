class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first, second = s[:len(s)//2], s[len(s)//2:]
        return sum([1 for c in first if c in 'aeiouAEIOU']) == sum([1 for c in second if c in 'aeiouAEIOU'])
