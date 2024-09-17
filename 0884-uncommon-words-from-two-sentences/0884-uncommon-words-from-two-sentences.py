class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a1, a2 = s1.split(), s2.split()
        c1, c2 = Counter(a1), Counter(a2)
        res = []
        
        for i in c1:
            if i not in c2 and c1[i] == 1:
                res.append(i)
        
        for i in c2:
            if i not in c1 and c2[i] == 1:
                res.append(i)
                
        return res