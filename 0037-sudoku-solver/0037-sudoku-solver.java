class Solution {
    public void solveSudoku(char[][] board) {
        if (board == null || board.length == 0) return;
        solve(board);
    }
    
    public boolean solve(char[][] board){
        for (int i=0; i < 9; i++){
            for (int j=0; j < 9; j++){
                if (board[i][j] == '.'){
                    for (char c='1'; c <= '9'; c++){
                        if (isValid(board, i, j, c)){
                            board[i][j] = c;
                            if (solve(board)) return true;
                            else board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    public boolean isValid(char[][] board, int row, int col, char c){
        for (int i=0; i < 9; i++){
            if (board[i][col] != '.' && board[i][col] == c) return false;
            if (board[row][i] != '.' && board[row][i] == c) return false;
            int b1 = (row / 3) * 3 + i / 3;
            int b2 = (col / 3) * 3 + i % 3;
            if (board[b1][b2] != '.' && board[b1][b2] == c) return false;
        }
        return true;
    }
}