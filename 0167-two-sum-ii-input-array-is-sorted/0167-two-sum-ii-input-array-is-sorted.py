class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if str(numbers[i]) in complements.keys():
                return [complements.get(str(numbers[i]))+1, i+1]
            else:
                complements[str(complement)] = i