from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return (c1.keys() == c2.keys()) and (sorted(c1.values()) == sorted(c2.values()))


# true
# test1
# a = "aabbbc"
# b = "abbccc"

# false
# test2
# a = "aabbczz"
# b = "abbczzz"

# true
# test3
a = "zzazicgvzwntnneauziwfzlrzkynzschzdkbmpqbolwgvxjava"
b = "uequrwuzhaudmnuqjuolkeszcyfqzqizrdrxpuvuygytbucwog"

solution = Solution()
print(solution.closeStrings(a, b))
