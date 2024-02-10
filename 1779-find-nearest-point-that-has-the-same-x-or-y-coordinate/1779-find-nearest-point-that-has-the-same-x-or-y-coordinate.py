class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_d = float('inf')
        ind = -1
        for i in points:
            if i[0] == x or i[1] == y:
                if abs(i[0]-x) + abs(i[1]-y) < min_d:
                    min_d = abs(i[0]-x) + abs(i[1]-y)
                    ind = points.index(i)
        return ind