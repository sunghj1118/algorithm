class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        char_count = {}

        # Count the number of times each character appears in the list of words
        for word in words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        # If the number of times a character appears is not divisible by the number of words, return False
        for char in char_count:
            if char_count[char] % len(words) != 0:
                return False

        return True


solution = Solution()
print(solution.makeEqual(["abc", "aabc", "bc"]))  # True
