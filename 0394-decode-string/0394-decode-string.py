class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(i: int) -> tuple[str, int]:
            result = ""
            k = 0

            while i < len(s):
                if s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                elif s[i] == '[':
                    i += 1
                    decoded_string, i = helper(i)
                    result += decoded_string * k
                    k = 0
                elif s[i] == ']':
                    i += 1
                    return result, i
                else:
                    result += s[i]
                    i += 1
            
            return result, i

        decoded, _ = helper(0)
        return decoded