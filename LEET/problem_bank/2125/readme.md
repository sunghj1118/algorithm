# 2125. Problem Review

## 2125. Number of Laser Beams in a Bank

### Problem Definition
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.


### Approach
- We need to compare between the two closest rows.
- If the next row doesn't have any devices, then it shouldn't be taken into account.
- Thus, we need to check if the row is all 0 or not.
- We also need to cycle through each row and only handle those that have devices.
- We could change the strings into a list of the sums of 1's (devices).
- The amount of beams would be the product between the sums.

### Solution
- Changed initial intuition.
- Create a list with the sum of all 1's in the 01 string.
    - Only append when the sum is not 0.
- Add the products between adjacent rows and return it.

```python
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
