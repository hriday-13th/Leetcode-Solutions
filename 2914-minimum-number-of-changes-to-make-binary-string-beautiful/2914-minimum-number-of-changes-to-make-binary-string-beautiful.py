class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            sub = s[i : i + 2]
            if sub == "00" or sub == "11":
                continue
            else:
                res += 1
                
        return res