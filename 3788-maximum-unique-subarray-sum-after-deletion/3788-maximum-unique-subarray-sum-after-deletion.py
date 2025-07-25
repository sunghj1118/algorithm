class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set()
        total = 0

        for num in nums:
            if num > 0 and num not in unique:
                total += num
            unique.add(num)
        
        if max(unique) < 0:
            return max(unique)

        return total