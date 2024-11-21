class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        layout = [[0 for i in range(n)] for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i, j in guards:
            layout[i][j] = 1
        for i, j in walls:
            layout[i][j] = 2

        def dfs(i, j, direction):
            if i < 0 or i >= m or j < 0 or j >= n or layout[i][j] == 1 or layout[i][j] == 2:
                return
            layout[i][j] = 3
            dfs(i + direction[0], j + direction[1], direction)

        for i, j in guards:
            for d in directions:
                dfs(i + d[0], j + d[1], d)

        count = 0
        for i in range(m):
            for j in range(n):
                if layout[i][j] == 0:
                    count += 1

        return count