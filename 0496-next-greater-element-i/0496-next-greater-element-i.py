class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        stack = []
        
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    found = False
                    for k in range(j+1, m):
                        if nums2[k] > nums1[i]:
                            stack.append(nums2[k])
                            found = True
                            break
                    if not found:
                        stack.append(-1)
                    break
        
        return stack