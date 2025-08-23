class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        current_zeroes = 0

        for num in nums:
            if num==0:
                current_zeroes += 1
                count += current_zeroes
            else:
                current_zeroes = 0
        
        return count