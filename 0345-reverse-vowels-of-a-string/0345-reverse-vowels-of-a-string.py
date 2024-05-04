class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = []
        
        for i in s:
            if i in "aeiouAEIOU":
                vows = [i] + vows
                
        count = 0
        res = list(s)
        for j in range(len(s)):
            if res[j] in "aeiouAEIOU":
                res[j] = vows[count]
                count += 1
                
        return "".join(res)