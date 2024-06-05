class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        d = defaultdict(list)
        
        for i in range(len(words)):
            d[i] = Counter(words[i])
            
        for ch in words[0]:
            same = True
            for i in range(len(words)):
                if d[i][ch] <= 0:
                    same = False
                    break
                d[i][ch] -= 1
            if same:
                res.append(ch)
                
        return res