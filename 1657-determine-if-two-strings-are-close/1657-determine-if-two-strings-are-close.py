class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        s1 = sorted(c1.values())
        s2 = sorted(c2.values())
        
        is_key = set(c1.keys()) == set(c2.keys())
        
        return s1 == s2 and is_key