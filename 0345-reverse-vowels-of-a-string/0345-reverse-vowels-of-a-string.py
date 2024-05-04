class Solution:
    def reverseVowels(self, s: str) -> str:
        w = list(s)
        vows = "aeiouAEIOU"
        i, j = 0, len(w) - 1
        
        while i <= j:
            while i < j and w[i] not in vows:
                i += 1
            while i < j and w[j] not in vows:
                j -= 1
            w[i], w[j] = w[j], w[i]
            i += 1
            j -= 1
            
        return "".join(w)