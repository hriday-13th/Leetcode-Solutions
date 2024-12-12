class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp1 = [0] * (len(text1) + 1)
        
        for i in range(1, len(text2) + 1):
            dp2 = [0] * (len(text1) + 1)
            for j in range(1, len(text1) + 1):
                if text2[i-1] == text1[j-1]:
                    dp2[j] = dp1[j-1] + 1
                else:
                    dp2[j] = max(dp2[j-1], dp1[j])
            dp1 = dp2
            
        return max(dp1)