class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis = []
        for i in matrix:
            lis.extend(i)
        lis.sort()
        return lis[k - 1]