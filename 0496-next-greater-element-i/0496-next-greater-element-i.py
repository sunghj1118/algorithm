class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        next_greater = {}
        stack = []

        # traverse nums2 and build a map of next greater elements
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        # for numbers that have no greater number, assign -1
        for num in stack:
            next_greater[num] = -1
        
        return [next_greater[num] for num in nums1]