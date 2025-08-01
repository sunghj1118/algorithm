class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_index = defaultdict(int)
        t_index = defaultdict(int)
        
        for i in range(len(s)):
            s_index[s[i]] = i
            t_index[t[i]] = i
        
        total = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for ch in alphabet:
            total += abs(s_index[ch] - t_index[ch])
        
        return total