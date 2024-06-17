class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        arr = [[0] * col for _ in range(row)]
        
        f1, f2 = True, True
        for i in range(col):
            if obstacleGrid[0][i] == 1:
                f1 = False
            arr[0][i] = 1 if f1 else 0
            
                
        for j in range(row):
            if obstacleGrid[j][0] == 1:
                f2 = False
            arr[j][0] = 1 if f2 else 0

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    arr[i][j] = 0
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
                
        return arr[-1][-1]