class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        diff_idx = 0
        first = -1
        second = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_idx += 1
                if first == -1:
                    first = i
                elif second == -1:
                    second = i
                else:
                    return False
        
        if s1[first] != s2[second] or s1[second] != s2[first]:
            return False

        return True
            
            