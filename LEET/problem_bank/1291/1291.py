from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Initialize an empty list to store the output
        output = []

        # Loop over the lengths of the numbers from low to high
        for length in range(len(str(low)), len(str(high)) + 1):

            # Iterate over the possible starting digits
            for start in range(1, 10):
                # Generate a sequential number of the current length starting with the current digit
                num = int(''.join(str(start + i) for i in range(length)))
                if start + length > 10:  # if the number contains a digit greater than 9, break the loop
                    break

                # If the number is within the range, append it to the output list
                if low <= num <= high:
                    output.append(num)
        # Sort the output list and return it
        return sorted(output)


print(Solution().sequentialDigits(100, 300))  # [123, 234]
