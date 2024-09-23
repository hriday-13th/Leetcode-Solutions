class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for word in dictionary:
                if s[i - len(word):i] == word and i >= len(word):
                    dp[i] = min(dp[i], dp[i - len(word)])

        return dp[n]
#         n = len(s)
#         dp = [0] * (n + 1)
        
#         for i in range(len(s)):
#             dp[i] = dp[i-1] + 1
#             for word in dictionary:
#                 if s[i:].startswith(word) and i >= len(word):
#                     dp[i] = min(dp[i], dp[i - len(word)])
                    
#         return dp[n]