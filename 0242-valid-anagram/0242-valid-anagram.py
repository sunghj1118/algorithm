class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts, t_counts = Counter(s), Counter(t)
        
        for count in s_counts:
            if count in t_counts:
                if s_counts[count] != t_counts[count]:
                    return False
            else:
                return False
        
        if len(s) != len(t):
            return False
        
        return True