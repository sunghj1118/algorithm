class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i=0; i<9; i++){
            Set<Character> set = new HashSet<>();
            for (int j=0; j<9; j++){
                char value = board[i][j];
                if (value == '.') continue;
                
                if (set.contains(value)){
                    return false;
                };
                set.add(value);
            }
        }

        for (int i=0; i<9; i++){
            Set<Character> set = new HashSet<>();
            for (int j=0; j<9; j++){
                char value = board[j][i];
                if (value == '.') continue;

                if (set.contains(value)){
                    return false;
                }
                set.add(value);
            }
        }

        for (int i=0; i<9; i++){
            Set<Character> set = new HashSet<>();
            int row = (i/3) * 3;
            int col = (i%3) * 3;

            for (int j=0; j<3; j++){
                for (int k=0; k<3; k++){
                    char value = board[row+j][col+k];
                    if (value=='.') continue;
                    if (set.contains(value)){
                        return false;
                    }
                    set.add(value);
                }
            }
        }

        return true;
    }
}