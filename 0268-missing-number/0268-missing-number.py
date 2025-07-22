class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if nums[-1] != n:
            return n

        for i in range(n+1):
            if i != nums[i]:
                return i

        return 0