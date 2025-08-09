class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]

        q = deque()
        visited = set()

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        dis = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if mat[i][j] == 1:
                    result[i][j] = dis
                
                for dr,dc in directions:
                    nr,nc = i+dr, j+dc
                    
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            dis += 1

        return result