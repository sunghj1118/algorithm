class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vals = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in vals:
                vals.remove(s[left])
                left += 1
            vals.add(s[right])
            max_len = max(max_len, right-left+1)
        
        return max_len