from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = Counter(s)
        count = 0

        for index, letter in enumerate(s):
            if dict_s[letter] == 1:
                return index

        return -1


s = "leetcode"
print(Solution().firstUniqChar(s))
