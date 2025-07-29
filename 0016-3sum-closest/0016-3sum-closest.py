class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        final = 0
        
        for i in range(n-2):
            left, right = i+1, n-1

            while left<right:
                total = nums[left] + nums[right] + nums[i]
                remainder = abs(target - total)

                if remainder < min_diff:
                    min_diff = remainder
                    final = total

                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return final
                