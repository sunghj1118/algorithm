class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        keys = sorted(set(nums))

        left = 0
        max_len = 1

        for right in range(1, len(keys)):
            if keys[right] - keys[right-1] != 1:
                left = right
            max_len = max(max_len, right-left+1)
        
        return max_len