class Solution(object):
    def getRow(self, n):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1], [1,1]]
        for i in range(2, n+1):
            k = [res[-1][i] + res[-1][i+1] for i in range(len(res[-1])-1)]
            k = [1] + k + [1]
            res.append(k)
        return res[n]