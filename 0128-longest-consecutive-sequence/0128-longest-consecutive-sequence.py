class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()

        vals = {}
        for i in range(len(nums)):
            vals[nums[i]] = vals.get(nums[i], 1)

        left = 0
        max_len = 1
        keys = list(vals)

        for right in range(1, len(keys)):
            if keys[right] - keys[right-1] != 1:
                left = right
            else:
                max_len = max(max_len, right-left+1)
        
        return max_len