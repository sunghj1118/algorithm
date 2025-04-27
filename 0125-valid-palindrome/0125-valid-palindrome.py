class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(char for char in s if char.isalnum()).lower()

        start = 0
        end = len(text) - 1

        while start < end:
            if text[start] == text[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True