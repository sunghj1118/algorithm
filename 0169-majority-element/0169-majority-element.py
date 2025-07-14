class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for count in counts:
            if counts[count] > len(nums)/2:
                return count