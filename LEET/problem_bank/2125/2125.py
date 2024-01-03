from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank_sums = []

        # Create a list of amount of devices in each row
        for i in range(len(bank)):
            row_sum = sum([int(c) for c in bank[i]])
            if row_sum != 0:
                bank_sums.append(row_sum)

        # Calculate the sum of the products between adjacent non-zero rows (beams)
        beams = 0
        for i in range(len(bank_sums) - 1):
            beams += bank_sums[i] * bank_sums[i + 1]

        return beams


solution = Solution()
print(solution.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
