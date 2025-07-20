class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        n = len(nums)

        for i, val in enumerate(nums):
            if val in indices and abs(indices[val] - i) <= k:
                return True
            indices[val] = i
        
        return False