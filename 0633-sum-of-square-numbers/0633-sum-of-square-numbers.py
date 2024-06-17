class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lis = [i for i in range(0, int(c**0.5) + 1)]

        i, j = 0, len(lis) - 1

        while i <= j:
            s = lis[i] ** 2 + lis[j] ** 2
            if s == c:
                return True
            elif s < c:
                i += 1
            else:
                j -= 1

        return False