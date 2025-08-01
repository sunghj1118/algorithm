class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]

        pyramid = [[1]]
        for i in range(1,numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = pyramid[i-1][j-1] + pyramid[i-1][j]
            pyramid.append(row)
        
        return pyramid