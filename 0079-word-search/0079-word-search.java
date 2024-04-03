class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        int len = word.length();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (backtrack(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    private boolean backtrack(char[][] board, String word, int i, int j, int k) {
        int rows = board.length;
        int cols = board[0].length;
        
        if (k == word.length()) {
            return true;
        }
        
        if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != word.charAt(k)) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '.';
        
        boolean found = backtrack(board, word, i + 1, j, k + 1) || 
                        backtrack(board, word, i - 1, j, k + 1) || 
                        backtrack(board, word, i, j + 1, k + 1) || 
                        backtrack(board, word, i, j - 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
}