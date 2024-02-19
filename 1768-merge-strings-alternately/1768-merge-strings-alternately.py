from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for a, b in zip_longest(word1, word2):
            if a is not None:
                res += a
            if b is not None:
                res += b
        return res