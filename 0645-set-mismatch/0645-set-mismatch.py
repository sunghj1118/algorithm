class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        duplicate = None
        loss = None
        
        for i in range(1, len(nums)+1):
            if counts[i] == 2:
                duplicate = i
            elif counts[i] == 0:
                loss = i
        
        return [duplicate, loss]