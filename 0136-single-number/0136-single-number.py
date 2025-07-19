class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = set()
        for i in range(len(nums)):
            if nums[i] in counts:
                counts.remove(nums[i])
            else:
                counts.add(nums[i])
        
        return counts.pop()
        

