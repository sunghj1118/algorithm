class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 rows
        # 9 cols
        # 9 boxes
        # for each num, check if it is possible
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                # find sub box (012,345,678)
                box_idx = (i // 3) * 3 + (j // 3)
                
                # check for duplicates
                # same row, same col, same box
                if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_idx]):
                    return False
                
                # if condition passed, add to set, allowing O(1) lookup
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        
        return True

        # example:
        # [0][1] = 3
        # check row: only 5
        # check col: nothing
        # check box: only 5
        # add to set
