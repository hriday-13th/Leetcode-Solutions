class Solution(object):
    def matrixSumQueries(self, n, queries):
        seenrows, seencols = set(), set()
        res = 0
        
        for q, i, val in queries[::-1]:
            if q == 0 and i not in seenrows:
                seenrows.add(i)
                res += val * (n - len(seencols))
            elif q == 1 and i not in seencols:
                seencols.add(i)
                res += val * (n - len(seenrows))
                
        return res