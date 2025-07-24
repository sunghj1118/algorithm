class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = set()
        values = {}
        earliest = 0
        
        for i in range(len(s)-1, -1,-1):
            if s[i] in unique:
                values[s[i]] = -1
            else:
                values[s[i]] = i
                unique.add(s[i])
                
        candidates = [idx for idx in values.values() if idx != -1]
        
        if not candidates:
            return -1
        
        return min(candidates)