class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_val = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_val = min(min_val, right-left+1)
                total -= nums[left]
                left += 1
        
        return 0 if min_val==float('inf') else min_val