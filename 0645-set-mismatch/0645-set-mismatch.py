class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        duplicate = counts.most_common(1)[0][0]
        
        unique = set(nums)
        for i in range(1, len(nums)+1):
            if i not in unique:
                loss = i
        
        return [duplicate, loss]