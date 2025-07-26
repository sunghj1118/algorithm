class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr2 = [0 for _ in range(len(nums))]
        even_pointer= 0
        odd_pointer = len(nums)-1
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                arr2[even_pointer] = nums[i]
                even_pointer += 1
            else:
                arr2[odd_pointer] = nums[i]
                odd_pointer -= 1
        
        return arr2