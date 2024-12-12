class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        prev = [0] * (len(text2) + 1)

        for i in range(1, len(text1) + 1):
            curr = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return prev[len(text2)]