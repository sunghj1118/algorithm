class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = 0
        strs = ""
        
        for ch in s:
            if ch.isdigit():
                nums = nums * 10 + int(ch)
            elif ch == '[':
                stack.append((strs, nums))
                strs = ""
                nums = 0
            elif ch == ']':
                last_str, num = stack.pop()
                strs = last_str + num * strs
            else:
                strs += ch
        
        return strs