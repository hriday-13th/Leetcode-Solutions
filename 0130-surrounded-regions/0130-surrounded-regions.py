class Solution:
    def bfs(self, board, a, b):
        q = deque([(a, b)])
        board[a][b] = "V"
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        while q:
            r, c = q.popleft()
            for ir, ic in directions:
                nr, nc = r + ir, c + ic
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == "O":
                        q.append((nr, nc))
                        board[nr][nc] = "V"
    
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        if rows == 0 or cols == 0:
            return
        
        for i in range(rows):
            if board[i][0] == "O":
                self.bfs(board, i, 0)
            if board[i][cols-1] == "O":
                self.bfs(board, i, cols - 1)
                
        for i in range(cols):
            if board[0][i] == "O":
                self.bfs(board, 0, i)
            if board[rows-1][i] == "O":
                self.bfs(board, rows - 1, i)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "V":
                    board[i][j] = "O"