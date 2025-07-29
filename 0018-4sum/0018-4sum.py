class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        if n < 4:
            return []
        elif n == 4 and sum(nums) == target:
            return [nums]
        
        for i in range(n-3):
            for j in range(i+1,n-2):
                left, right = j+1, n-1

                while left<right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    comb = [nums[i], nums[j], nums[left], nums[right]]

                    if total == target and comb not in result:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result