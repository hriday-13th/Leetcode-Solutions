class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        l1, l2 = s1.split(), s2.split()
        
        if len(l1) < len(l2):
            l1, l2 = l2, l1
            
        i = 0
        while i < len(l2) and l1[i] == l2[i]:
            i += 1
            
        j = 0
        while j < len(l2) and l1[-j - 1] == l2[-j - 1]:
            j += 1
            
        return i + j >= len(l2)