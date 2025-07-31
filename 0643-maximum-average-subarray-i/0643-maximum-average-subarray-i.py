class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum/k

        for right in range(k, len(nums)):
            window_sum = window_sum + nums[right] - nums[right-k]
            max_avg = max(window_sum/k, max_avg)
        
        return max_avg