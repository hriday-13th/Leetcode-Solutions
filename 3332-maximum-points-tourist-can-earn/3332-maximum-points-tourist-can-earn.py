class Solution:
    def maxScore(self, n: int, k: int, stay: List[List[int]], travel: List[List[int]]) -> int:
        dp = [0] * n
        
        for i in range(k):
            dp2 = dp[:]
            for curr in range(n):
                dp2[curr] += stay[i][curr]
            for curr in range(n):
                for dest in range(n):
                    if curr != dest:
                        dp2[dest] = max(dp2[dest], dp[curr] + travel[curr][dest])
            dp = dp2
        
        return max(dp)