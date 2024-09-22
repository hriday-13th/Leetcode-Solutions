class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l, r = 0, 0
        d = Counter(word2)
        l1 = len(word1)
        req = len(word2)
        res = 0
        
        while r < l1:
            if word1[r] in d:
                if d[word1[r]] > 0:
                    req -= 1
                d[word1[r]] -= 1
                
            r += 1
            
            while req == 0:
                res += l1 - r + 1
                if word1[l] in d:
                    d[word1[l]] += 1
                    if d[word1[l]] > 0:
                        req += 1
                l += 1
            
        return res