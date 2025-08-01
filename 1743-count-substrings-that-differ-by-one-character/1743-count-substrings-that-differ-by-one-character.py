class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        result = 0
        n, m = len(s), len(t)

        for i in range(n):
            for j in range(m):
                diff = 0
                k = 0
                while i+k<n and j+k<m:
                    if s[i+k] != t[j+k]:
                        diff += 1
                    if diff > 1:
                        break
                    if diff == 1:
                        result += 1
                    k += 1
        
        return result