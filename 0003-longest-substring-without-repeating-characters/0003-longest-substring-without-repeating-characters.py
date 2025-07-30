class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            right = i+1
            substr = set()
            substr.add(s[i])
            len_substr = 1

            while right < n:
                if s[right] in substr:
                    break
                
                substr.add(s[right])
                len_substr += 1
                right += 1
            
            max_len = max(max_len, len_substr)
        
        return max_len
