class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        left, right = 0, len(haystack) - len(needle)

        while left<=right:
            if haystack[left:left+len(needle)] == needle:
                return left
            left += 1
        
        return -1