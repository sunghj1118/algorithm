class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter+=1
            else:
                zeros += 1
        
        for i in range(zeros):
            nums[-(i+1)] = 0