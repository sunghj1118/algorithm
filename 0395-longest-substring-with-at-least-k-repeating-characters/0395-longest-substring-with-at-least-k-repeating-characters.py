class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        
        for target_unique in range(1,27):
            unique_chars = 0
            chars_at_least_k = 0

            left = 0
            right = 0
            count = {}
            while right < n:
                count[s[right]] = count.get(s[right], 0) + 1
                
                if count[s[right]] == 1:
                    unique_chars += 1
                if count[s[right]] == k:
                    chars_at_least_k += 1

                while unique_chars > target_unique:
                    count[s[left]] -= 1
                    if count[s[left]] == k-1:
                        chars_at_least_k -= 1
                    if count[s[left]] == 0:
                        unique_chars -= 1
                        del count[s[left]]
                    left += 1
                
                if unique_chars == chars_at_least_k:
                    max_len = max(max_len, right-left+1)
                
                right += 1
        
        return max_len
        
