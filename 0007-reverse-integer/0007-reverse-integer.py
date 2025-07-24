class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1
        
        
        str_x = str(x)
        negative = False
        
        if str_x[0] == '-':
            negative = True
            str_x = str_x[1:]
        
        reversed_str = str_x[::-1]
        reversed_int = int(reversed_str)
        
        if negative:
            reversed_int = -reversed_int
        
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        return reversed_int