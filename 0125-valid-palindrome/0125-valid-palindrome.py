class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = ''.join(ch for ch in s if ch.isalnum()).lower()
        l,r = 0, len(parsed)-1
        
        while l<r:
            if parsed[l] != parsed[r]:
                return False
            l+=1
            r-=1
        
        return True