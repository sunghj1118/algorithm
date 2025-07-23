class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        longest = 0
        odd_count = 0

        for i, val in enumerate(letters):
            if letters[val] % 2 == 0:
                longest += letters[val]
            else:
                longest += letters[val] - 1
                odd_count = 1

        longest += odd_count
        
        return longest