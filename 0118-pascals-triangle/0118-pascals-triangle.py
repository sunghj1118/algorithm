class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pyramid = []
        for i in range(numRows):
            row = [1]

            if i > 0:
                for j in range(1, i):
                    row.append(pyramid[i-1][j] + pyramid[i-1][j-1])
                row.append(1)
            
            pyramid.append(row)
        
        return pyramid