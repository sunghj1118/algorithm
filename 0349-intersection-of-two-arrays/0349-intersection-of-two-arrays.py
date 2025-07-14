class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        set1 = set(nums1)
        set2 = set(nums2)

        for i in set1:
            if i in set2:
                intersection.append(i)
        
        return intersection