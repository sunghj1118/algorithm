class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        for i in range(9):
            row = set()
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row:
                    return False
                row.add(val)
        
        # check vertical
        for i in range(9):
            col = set()
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if val in col: 
                    return False
                else:
                    col.add(val)

        # check square
        square = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in square[i//3][j//3]:
                    return False
                else:
                    square[i//3][j//3].add(board[i][j])

        return True