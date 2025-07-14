class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for num in counts:
            if counts[num] >= 2:
                return True
        
        return False