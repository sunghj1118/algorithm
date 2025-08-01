class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_index = {ch:i for i,ch in enumerate(s)}
        t_index = {ch:i for i,ch in enumerate(t)}
        
        return sum(abs(t_index[ch] - s_index[ch]) for ch in s)