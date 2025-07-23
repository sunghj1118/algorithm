class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0

        for i in range(len(nums) // 2):
            total += nums[i*2]
        
        return total