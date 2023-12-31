class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        max_length = -1
        char_index_map = {}

        for i, char in enumerate(s):
            if char in char_index_map:
                max_length = max(max_length, i - char_index_map[char] - 1)
            else:
                char_index_map[char] = i

        return max_length
