class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1,1]]

        res = [[1], [1,1]]
        for i in range(2, n):
            k = [res[-1][i] + res[-1][i+1] for i in range(len(res[-1])-1)]
            k = [1] + k + [1]
            res.append(k)
        return res