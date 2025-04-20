class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        if n <= 1:
            return s
        
        # repeat n-1 times
        for i in range(n-1):
            # check for consecutive identical integers
            # compare i for n values in the string
            result = ""
            current_char = s[0]
            count = 1
            for char in s[1:]:
                if char == current_char: #curr char == next char
                    count += 1
                else: #append all reps until now, change next char
                    result = result + str(count)
                    result = result + str(current_char)
                    current_char = char
                    count = 1
            result = result + str(count)
            result = result + str(current_char)

            s = result
        
        return s
            


