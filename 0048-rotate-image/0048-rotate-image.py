class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix)-1
        
        while l<r:
            for i in range(r-l):
                top, bottom = l,r
                
                # store temp value
                topLeft = matrix[top][l+i]
                
                # replace topLeft with bottomLeft
                matrix[top][l+i] = matrix[bottom-i][l]
                
                # replace bottomLeft with bottomRight
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                # replace bottomRight with topRight
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # replace topRight with topLeft
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1