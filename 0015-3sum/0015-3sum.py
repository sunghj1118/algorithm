class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            left, right = i+1, len(nums)-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left_val = nums[left]
                    right_val = nums[right]
                    while left<right and nums[left] == left_val:
                        left += 1
                    while left<right and nums[right] == right_val:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result