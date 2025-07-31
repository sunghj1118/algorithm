class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt_s1 = Counter(s1)
        window_count = defaultdict(int)
        required = len(cnt_s1)
        formed = 0
        left = 0
        
        for right in range(len(s2)):
            char = s2[right]
            window_count[char] += 1

            if char in cnt_s1 and window_count[char] == cnt_s1[char]:
                formed += 1
            
            while (right-left+1) > len(s1):
                left_char = s2[left]

                if left_char in cnt_s1 and window_count[left_char] == cnt_s1[left_char]:
                    formed -= 1
                
                window_count[left_char] -= 1
                left += 1
            
            if formed==required and (right-left+1)==len(s1):
                return True
        
        return False
