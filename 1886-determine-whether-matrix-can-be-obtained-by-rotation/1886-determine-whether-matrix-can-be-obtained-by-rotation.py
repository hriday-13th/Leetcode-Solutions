class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        temp = [[y for y in x] for x in mat]
        n = len(mat)
        rotation = 1
        while rotation < 5:
            for i in range(n):
                for j in range(n):
                    mat[j][n - 1 - i] = temp[i][j]
            if mat == target:
                return True
                break
            temp = [[y for y in x] for x in mat]
            rotation += 1
        return False