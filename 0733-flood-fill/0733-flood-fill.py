class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image

        stack = [(sr,sc)]

        while stack:
            r,c = stack.pop()

            if (r<0 or r>= rows or c < 0 or c >= cols or image[r][c] != original_color):
                continue
            image[r][c] = color
            stack.append((r+1, c))
            stack.append((r-1, c))
            stack.append((r, c+1))
            stack.append((r, c-1))
        
        return image