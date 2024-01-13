class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_s = {}
        dict_t = {}

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1

        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        for char in dict_s:
            if char in dict_t:
                dict_s[char] -= dict_t[char]

        pos_count = sum(v for v in dict_s.values() if v > 0)
        neg_count = sum(v for v in dict_s.values() if v < 0)

        if pos_count >= neg_count:
            return pos_count
        else:
            return abs(neg_count)


s = "anagram"
t = "mangaar"

solution = Solution()
print(solution.minSteps(s, t))
