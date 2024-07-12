class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        d = defaultdict(lambda : 0)
        cnt = Counter(targetWords)
        targetWords = set(targetWords)
        for i in targetWords:
            m = "".join(sorted(i))
            d[m] += cnt[i]
            
        res = 0
        startWords = set(startWords)
        for word in startWords:
            for j in range(26):
                x=word+chr(97+j)
                x="".join(sorted(x))
                if d[x]>0:
                    res+=d[x]
                    d[x]=0
                    
        return res