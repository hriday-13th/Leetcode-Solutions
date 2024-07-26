class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            matrix[i][i] = 0
            
        for i, j, w in edges:
            matrix[i][j] = w
            matrix[j][i] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
            
        minReachableCities = float('inf')
        bestCity = -1
        
        min_city = float('inf')
        city = -1
        
        for i in range(n):
            reach = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    reach += 1
                    
            if reach <= min_city:
                min_city = reach
                city = i
                    
        return city