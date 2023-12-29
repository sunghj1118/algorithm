class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        str_arr = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                str_arr.append("FizzBuzz")
            elif i % 3 == 0:
                str_arr.append("Fizz")
            elif i % 5 == 0:
                str_arr.append("Buzz")
            else:
                str_arr.append(str(i))

        return str_arr


solution = Solution()
print(solution.fizzBuzz(15))  # Example input
