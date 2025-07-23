class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        li = [0 for _ in range(n+1)]
        lo, hi = 0,n

        for i in range(n):
            if s[i] == 'I':
                li[i] = lo
                lo += 1
            else:
                li[i] = hi
                hi -= 1
        
        li[n] = lo
        
        return li