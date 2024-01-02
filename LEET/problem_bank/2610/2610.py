class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqdict = {}
        for num in nums:
            if num in freqdict:
                freqdict[num] += 1
            else:
                freqdict[num] = 1

        result = []
        while freqdict:
            row = []
            # Iterate over the items in the dictionary
            for num in list(freqdict.keys()):
                row.append(num)
                freqdict[num] -= 1
                # Remove the item from the dictionary if the count is 0
                if freqdict[num] == 0:
                    del freqdict[num]
            result.append(row)

        return result
