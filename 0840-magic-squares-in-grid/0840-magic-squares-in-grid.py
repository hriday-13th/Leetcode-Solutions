class Solution:
    def isMagical(self, grid, a, b):
        nums = [False] * 10
        rowSum = [0] * 3
        colSum = [0] * 3
        diaSum = [0] * 2

        for i in range(3):
            for j in range(3):
                val = grid[a - 1 + i][b - 1 + j]

                if not (1 <= val <= 9):
                    return False

                if nums[val]:
                    return False
                nums[val] = True

                rowSum[i] += val
                colSum[j] += val

                if i == j:
                    diaSum[0] += val
                if i + j == 2:
                    diaSum[1] += val

        net = rowSum + colSum + diaSum

        return len(set(net)) == 1

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows < 3 or cols < 3:
            return 0

        count = 0

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if self.isMagical(grid, i, j):
                    count += 1

        return count