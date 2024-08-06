class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        lis = sorted(list(freq.values()), reverse=True)
        
        count = 0
        
        for i in range(len(lis)):
            if i < 8:
                count += lis[i]
            elif i < 16:
                count += lis[i] * 2
            elif i < 24:
                count += lis[i] * 3
            elif i < 26:
                count += lis[i] * 4
        
        return count