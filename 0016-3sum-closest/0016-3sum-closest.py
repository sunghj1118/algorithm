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
                min_diff = min(min_diff, remainder)
                final = total if min_diff >= remainder else final
                # print(nums[left],nums[right],nums[i], total,final)

                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return final
                