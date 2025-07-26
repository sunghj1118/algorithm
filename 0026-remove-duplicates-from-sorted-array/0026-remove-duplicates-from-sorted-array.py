class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        
        unique = set()
        counter = 0

        for num in nums:
            if num not in unique:
                unique.add(num)
                nums[counter] = num
                counter += 1

        return counter