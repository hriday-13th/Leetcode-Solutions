class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        q = deque()
        maxi = rows * cols
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = maxi
                    
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] > mat[i][j] + 1:
                    q.append((ni, nj))
                    mat[ni][nj] = mat[i][j] + 1
                    
        return mat