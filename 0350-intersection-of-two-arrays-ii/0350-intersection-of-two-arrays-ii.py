class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        for num1 in counter1:
            if num1 in counter2:
                for i in range(min(counter1[num1], counter2[num1])):
                    intersection.append(num1)
        
        return intersection